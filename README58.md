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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 641ba48f-6dbd-37a4-8889-1ecd30a01615 | -2.57687 | -48.3927 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38d8d0b7-0c17-3e2e-9806-0be3833582f7 | -0.96869 | -51.72915 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6300c5f1-c1cb-39e6-a155-c40956276006 | -2.68543 | -46.23375 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3a3f9f4-61b1-3267-88f5-ce6454f17507 | -5.3764 | -50.4766 | 2024-11-20 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8385b8d5-11a7-3558-b99d-e2b0c1b18d78 | -3.6154 | -52.11574 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 574e58cf-1e55-3ebe-858a-95dd94a31799 | -5.45477 | -44.82404 | 2024-11-20 04:50:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa2a3c87-72a9-353f-a9cf-4b6af4b83873 | -1.51791 | -55.4841 | 2024-11-20 04:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7e65988-d342-3924-9c77-048dd31bab32 | -1.73494 | -53.02708 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc1146d8-b6cb-3388-b5c5-e4f31deb2cfd | -1.7056 | -50.20269 | 2024-11-20 04:50:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c88561d-04bf-395b-9f0b-42871a204260 | -2.92117 | -53.07747 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5514ee9e-df11-3846-bfe4-ec9c6c85db35 | -0.79902 | -51.23671 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34401149-5cb8-3de5-86b7-3d29c7ec7177 | -9.17192 | -44.73289 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cdd4f03-3fac-3616-ba5f-6dd7dbef5b55 | -2.68128 | -46.23313 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0b06ca1-8609-3ea7-9a1d-97228239b847 | -1.50518 | -51.18107 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f70b4beb-fb94-343d-ae4c-94ce83436f66 | -3.02774 | -51.5256 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91fb1d04-8d4b-371b-86aa-0613769203fa | -4.3828 | -47.75588 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd2add61-8f91-32ff-99fa-ae2053b64c28 | -3.50182 | -51.67694 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1950c26b-2b81-33a4-ad6c-33968b4dddff | -1.15257 | -53.51157 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a0d5f12-aaa2-393f-9403-4101df780773 | -2.82521 | -45.13372 | 2024-11-20 04:50:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46820084-7056-37e6-a78d-688562e04afb | -1.44873 | -54.50414 | 2024-11-20 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3753b0c1-2f38-33f3-801c-dd0eba8d59ec | -2.85117 | -53.97551 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 137a087d-4f25-3caf-ad13-f877bf0062d6 | -2.80707 | -54.02049 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6894f6e3-aa02-303d-a7de-4a3b5e11a72e | -1.3385 | -51.40213 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e94cef00-c76f-390b-bbfe-779e38a52bc6 | -1.94846 | -53.3343 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91ff9168-3ab3-3aa3-93e5-d36b61d5e9b0 | -2.75653 | -54.0679 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c937923-d165-3e32-a9b1-8be97ef14ac7 | -1.59929 | -53.08821 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22690c22-1c7d-3054-a143-c43ddf43a01a | -2.79905 | -51.79661 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 841d9655-61d9-3609-a880-4b2a250fca85 | -2.27326 | -48.45227 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5abef8e5-1d4a-32a5-879d-51575307e72a | -4.62944 | -49.54559 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92357f3e-11b5-354e-abd5-729e9982dea1 | -3.81595 | -51.35424 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 160bbfed-2d79-3f90-8c47-d9200a4d3693 | -2.82165 | -54.01887 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f56613e9-8305-35fd-b156-5e09a0c2dd65 | -2.56331 | -46.54692 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 519aa7ca-bbc9-39af-9b9f-b4ead267894d | -1.58128 | -50.43628 | 2024-11-20 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebb72e3d-b4b2-3e76-ab99-beb1161b3915 | -3.6352 | -51.01617 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bcc0c4b-12a5-3aab-83f3-e04936025497 | -9.17504 | -44.72107 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5897422e-8c3d-3dd8-b374-9e95a3cd1633 | -1.88409 | -50.96829 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 96f8a84c-067c-3bf2-9e2e-248d508e03e8 | -2.56655 | -49.20263 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be2a7bf4-4d26-3674-931a-b6dd8fc6d7c4 | -1.45989 | -52.68972 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f174b4a7-5e54-3fdb-990b-6b1c76967315 | -3.72641 | -47.36909 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89054a6b-0746-3991-a0e9-1f4538e7fc23 | -2.76126 | -54.06071 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b287b4-10e2-310b-9c7a-09b43610e6f2 | -2.41742 | -45.81868 | 2024-11-20 04:50:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d37a9f2-c8ff-32d9-88c8-cccd8529787f | -3.58388 | -53.72468 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a36dece-1561-3446-a7f1-e7130a64bf75 | -2.19961 | -53.66654 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c240ff8-fc87-396b-bb50-ea0f274e987a | -0.92784 | -52.47974 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 784ce87d-dad9-3c7f-8b93-c6de26695201 | -1.10276 | -51.73995 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc3fb556-a371-3a1b-9303-d08bec98e71a | -2.94884 | -48.32819 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a56515d-7705-3328-b588-e703c9ea1d67 | -2.73951 | -51.72371 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e5749bbd-46ef-3f00-a12a-26ee0330735e | -2.21038 | -53.71096 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11445c80-b65e-3f09-82ee-cee7c6b46e41 | -1.54643 | -52.27226 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab2ec75a-dbbe-3f38-87b9-8800d500625c | -1.31196 | -52.40826 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a65eb78a-e0e9-3ff4-9ce2-636f93e76d27 | -2.90431 | -53.05281 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f4c1136-91bb-3ff4-b402-6fc9b1241939 | -3.31266 | -54.74515 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ef57e1b9-5015-3711-bc91-f5a980089c21 | -2.58433 | -51.72086 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d760f2a2-dabe-3fd5-abca-ce759bceab73 | -0.8958 | -51.7215 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b992382-eb0d-39e7-84b0-d77c5185a4af | -2.2514 | -48.16132 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37a91071-1a6d-3522-947a-6fcd7d2b6f43 | -2.79628 | -51.79264 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ea15c66-25b2-3aba-8dbc-c95df7aba708 | -3.30019 | -49.04816 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c41c033-ca7f-346a-b362-d43d2e44b8fd | -4.07119 | -46.8488 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 029b9be8-0da1-3b68-86cf-8618efe5cf15 | -1.20222 | -51.77299 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0851cfcc-b961-356e-8440-dc79f4e9d1dd | -1.44604 | -55.06528 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eed9718-4b84-3ae2-add2-ab17b14d9eee | -5.96257 | -48.06025 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46d034bc-2a41-3823-9475-5e731b362988 | -2.19902 | -53.67031 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95d8bcfd-8e22-3961-b67c-2f45c58036e9 | -5.24733 | -42.6466 | 2024-11-20 04:50:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef30aadf-2952-3128-a77e-1374721ec910 | -1.20445 | -51.78043 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4ef537d-b297-3884-bd39-cb55be9445c1 | -6.82593 | -43.29087 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 526f7c91-6aad-3ac1-bafa-330359fee151 | -2.29639 | -49.06016 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c6fcbe3-9eed-3ff4-9f78-7127971c6ab6 | -4.46769 | -46.58455 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 884b2dbd-df2c-348b-a352-000f03f4b313 | -2.72187 | -49.34269 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2390a80a-85dd-350c-bee9-094ad82b922a | -1.31069 | -52.26389 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c1a1713-d1e8-3791-9adb-88cb0b0a98cc | -5.15218 | -44.12608 | 2024-11-20 04:50:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f127d4ff-a3ef-334b-87bb-743d047cf735 | -1.21667 | -51.78941 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d362f03f-ccee-3122-8a70-b5144a936214 | -2.72535 | -49.34322 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a102198e-5fb9-30f9-8f7c-ffd6129452e8 | -2.05899 | -53.42656 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4122b6dc-9652-3e5a-ac88-a58768f45e78 | -2.53815 | -54.55212 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34b81a7b-5cd5-316e-8e13-dbe402195df3 | -1.20331 | -51.76608 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34a00824-bdc0-32fb-ae0c-3858bac74eeb | -1.66396 | -52.65898 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dd80866-50f3-3ff7-9378-061e85df47d4 | -1.17098 | -53.67413 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778385ca-3e83-38cf-a8ae-72f0ee28d279 | -1.55087 | -52.26579 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46796e45-d20c-3052-b24d-be0804fe3877 | -1.20262 | -51.9826 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50d8182f-360f-342a-a939-1b59b0d44844 | -3.28708 | -53.83655 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 37e66473-79fe-39c7-aa14-f684ba54b398 | -3.47093 | -53.48897 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 594a25e8-9ba4-39c1-8ed2-953989db4bee | -3.80313 | -51.13873 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 125dac7e-2d5f-3390-8a01-bda5213612ca | -2.74716 | -51.82384 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 42f733b4-b236-38e5-9d87-3ec3aea56802 | -6.93264 | -41.20026 | 2024-11-20 04:50:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 24a28e2a-4aac-3162-896a-791c1fcd9f1f | -0.94576 | -51.63708 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4238ee0c-dd6b-30c1-b65c-1752370f43f1 | -4.39149 | -47.7766 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b1a06e4-ce64-30d2-a693-c8a4517c095a | -0.94319 | -51.71809 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42c9e12a-ddf3-34d4-bf72-75ee37f1c37e | -3.81052 | -52.29488 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21363eca-ece7-3215-9cb8-23b6760b9ee0 | -3.90783 | -52.40632 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0966d8d8-4a6a-381c-a050-1dc101ceb7e6 | -1.20881 | -51.75276 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cbf8daf-7349-35ba-8768-2c7b49ad8ec7 | -1.2447 | -53.36699 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 106e2792-d546-366c-9701-39260ab12506 | -2.26851 | -50.82208 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b55be1-0925-3039-82fe-e6e9314a9dd9 | -2.71898 | -49.33831 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00727ac6-edfb-3af8-98bf-154ad02ee8c2 | -2.0932 | -53.34462 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49d4670c-9e6a-3ddf-946e-9117c434f986 | -2.5527 | -53.98939 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0010e5b3-e22e-3d7f-b8c9-249f4948c356 | -3.32662 | -43.08468 | 2024-11-20 04:50:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1d31d30-5c91-3756-a12a-e86e13d55806 | -3.80536 | -51.14626 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5b5ed28-fcfe-38ed-99f2-cf322c26c451 | -2.69203 | -46.24611 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3988d6cd-15d4-3417-85c0-9dbf60877a48 | -2.64013 | -46.21647 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff6dd9f1-9009-3989-b044-be5f25db7348 | -3.56156 | -45.01741 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README59.md)
