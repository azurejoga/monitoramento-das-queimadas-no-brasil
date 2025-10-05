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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9bcea92f-f527-3ef0-b074-5097bac410b1 | -4.13694 | -47.65796 | 2025-10-05 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2db8c8ef-bca6-34e8-9f1a-55b8de948300 | -4.63972 | -43.18126 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3143f6b2-de21-3a85-9501-770973145877 | -3.78535 | -52.11889 | 2025-10-05 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b426eda6-67b4-36b9-8b4e-2eba6574a6f0 | -4.62931 | -43.19134 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d2408035-6267-339b-ab13-d60fd4880234 | -4.65314 | -43.19036 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 56c750b8-0104-3dfd-8bde-cefa52af742b | -4.31352 | -48.09133 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4843fb86-7262-333d-961e-ac76ca6d6a7e | -4.23401 | -46.75567 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 967b2964-c654-33e0-9e2f-8d6b7d781f9c | -4.63652 | -43.19227 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 456dd467-ffa5-3b40-9b8c-ffae2529437e | 0.44753 | -50.80262 | 2025-10-05 05:12:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68c726a6-52de-3ec1-9e85-9138200cace3 | -2.89347 | -50.73349 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0d23239-3187-308f-a570-f4672b1c58a6 | -3.61362 | -51.03902 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4dd6fbb-218d-3670-a590-3363223e2468 | -3.78619 | -43.57777 | 2025-10-05 05:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d130ecfb-cfe4-3f87-8ac3-1ff00183c896 | -3.95261 | -49.9011 | 2025-10-05 05:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52eb08c8-7651-39e5-9599-0db3c8287eb7 | -3.81513 | -51.07182 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 491f1057-cc9a-32fb-9bb8-c36f7aa16907 | -2.51607 | -51.93336 | 2025-10-05 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c9612dd-7d6f-38ca-be06-4d002ac087e3 | -4.25488 | -48.56934 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541da4c9-96f7-37f8-97f0-79d9d9ed8f29 | -4.43676 | -43.23721 | 2025-10-05 05:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 54fa8c4b-675f-3ce3-aee3-a50bcea6bf39 | -2.90206 | -50.73481 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f63d08b9-f665-3957-84f5-a2041951f257 | -3.0857 | -47.79114 | 2025-10-05 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35efd47d-af0b-3d0f-8399-eefb22f8c5c6 | -4.6437 | -43.19337 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9d8e0ab5-37f6-3c44-a808-778771f36c61 | -2.68813 | -48.39076 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c4f6c37f-c1ee-3462-9eb0-73d66139e448 | -2.904 | -48.07899 | 2025-10-05 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dae4c613-91bd-3ce6-8dc7-2174aaba435d | -3.04066 | -54.28682 | 2025-10-05 05:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5fc061f-16c9-3d54-b7e9-f5f906bf0331 | -4.22942 | -46.74668 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8b31636-b82b-37e7-80c8-01d2c349b9ca | -4.64577 | -43.17923 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3bf6522a-21ce-3734-862b-8e29ac8901b1 | -2.89407 | -50.72947 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31676438-db4d-3052-a5c9-34b99539b701 | -2.68728 | -48.39652 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84cc6544-c5c4-33b2-b576-22ab5ad673d7 | -4.2553 | -48.5664 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af95d5ce-827e-3f6f-b6e0-cd3fe266d0f8 | -2.29571 | -47.99576 | 2025-10-05 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c1a7a8f-3b00-3e0f-b5d7-d8444b6544be | -2.90145 | -50.73884 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9422094e-5758-3b07-8439-ac5e6eafa5c0 | -2.89286 | -50.73752 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a70067b-17ed-3280-8cf7-544b88fe9c3c | 0.52821 | -50.78674 | 2025-10-05 05:12:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4b68b15-372c-37c8-8c70-fc6faffa5641 | -2.941 | -51.27332 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ae67619-a0f6-3f3d-9a7d-c9bc8dad7105 | -2.89883 | -48.07824 | 2025-10-05 05:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67f6b67b-4418-3f9b-a087-8c2fddf692ce | -4.22829 | -46.75454 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05334aef-a5dc-3bd4-a5cc-68033d922afc | -3.81138 | -51.29715 | 2025-10-05 05:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dc71351-1838-3f7c-86e8-85058ab0956e | -2.29619 | -47.99269 | 2025-10-05 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9f9656d-dc67-3965-99a6-b82f6d1baffe | -4.63855 | -43.17831 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 896fd1b9-d3f8-3778-b1a9-0b2dd3f0148b | -3.68863 | -50.89145 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 176d56e2-312e-3623-8aaf-2bf54f6410d4 | -4.4449 | -43.2313 | 2025-10-05 05:12:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9f12f8a8-e36b-3049-8c0b-766cb59ab61c | -3.39742 | -50.27005 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b2423e6-773f-3e15-84d1-fa983daa316f | -2.52078 | -51.92903 | 2025-10-05 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d6f847-9874-3107-b435-3d62e897a556 | -4.64593 | -43.18938 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 62b2c639-8c08-3678-a12c-574c53a1bcbf | -2.89898 | -50.7261 | 2025-10-05 05:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bad3e68-c430-3a89-854c-788c3e98946e | -4.25339 | -48.56327 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6956b66-0325-33fb-8266-b494027bc6c4 | -3.83476 | -44.55213 | 2025-10-05 05:12:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0e4d74b-5838-3352-8d2d-8799b9387be2 | -2.68738 | -48.40133 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ffab558-e80d-3282-b3d4-18f2bb594a53 | -4.26923 | -46.75604 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf1b7852-668f-3e75-9b14-a47cd09cc3f4 | -2.68412 | -48.38916 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccef47b6-63d5-34e7-b18f-9a81eae50e98 | -4.27613 | -46.74908 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aae0bc4-ae71-36a7-810b-9734255e8aad | -4.23458 | -46.75169 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78808641-d738-3d71-857c-28981e7ca82a | -2.25009 | -47.87931 | 2025-10-05 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bec7a23f-ba75-3b27-b5e9-f11337261ea5 | -4.64693 | -43.18224 | 2025-10-05 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5417336e-3781-3d86-8588-6d8fc6047178 | -4.25938 | -48.5581 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22382b33-9186-3227-9b82-ecf7740292ba | -3.80525 | -51.76959 | 2025-10-05 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| e73d8bcb-d798-3f7b-834e-a46fc6d94e97 | -2.68225 | -48.39574 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ccc31cc-e522-32d3-af49-713cf1582e57 | -3.53937 | -49.51226 | 2025-10-05 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f88890c-1a84-3632-947c-b58ab913e2ea | -2.68323 | -48.39493 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab753a1f-f67c-3bd3-abfc-bc812aac19f5 | -4.22885 | -46.75062 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f37f5930-06b9-364b-a4f2-5c6c64a007bf | -3.09223 | -47.02118 | 2025-10-05 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f197387-c464-3cc7-bb10-fffe5d5cd9eb | -2.25528 | -47.88003 | 2025-10-05 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07cbe634-8152-3bed-9f15-351ba13ef4ed | -2.68826 | -48.39568 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ec6e946-7a47-35ac-a895-ce51f1618c6f | -3.08719 | -47.79157 | 2025-10-05 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1a8706a-e2d0-3e17-a9e4-90889d653eaf | -3.81085 | -51.07133 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 84538ba7-dfa2-3c37-ae4e-cd34e42c9984 | -4.27034 | -46.74844 | 2025-10-05 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea24e8ba-f73d-3b18-81da-2f7701c43583 | -0.91021 | -47.54779 | 2025-10-05 05:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af18ddeb-2dc4-3e62-987e-4b22be60d957 | -4.25251 | -48.56913 | 2025-10-05 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d56cdba-01af-3287-affe-be747a39eba6 | -2.6831 | -48.38995 | 2025-10-05 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f0674d5-8e4f-356a-a6ed-45640857e959 | -3.814 | -51.07934 | 2025-10-05 05:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 184e8f94-3f6d-3354-b421-4d97d2904a5a | -6.17917 | -44.58181 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b4f6eae-4dc7-3304-8c88-acd114b40c71 | -10.3979 | -45.41879 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ee9b173-e344-346f-b9ae-36262ac9007b | -11.83098 | -45.09194 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ae98fd-8e62-30f3-9cf4-4dbfc1d9720e | -8.54278 | -46.31654 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9eca5fa7-7ad7-3338-8fbc-0a2575afb4b7 | -8.56663 | -46.3297 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ee3e795-c90b-3eeb-aa23-adbb435e9a61 | -5.21399 | -46.18069 | 2025-10-05 05:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f1d0b2-742b-3e3c-a775-ac66e5d776bd | -10.45931 | -57.49979 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 181d4fc1-1a08-3044-b475-b683023ef373 | -7.7891 | -44.51962 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eda337a-b30e-3e33-b752-4b9931697ce7 | -10.3936 | -45.39749 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a14607b-12d7-3b6a-a8ca-a763699d5d3d | -5.88751 | -43.7117 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c36f4046-6767-3406-b4e2-f7377dbe06c7 | -10.39421 | -45.40027 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccf2b727-eb6a-3929-b2fa-d12415612e75 | -10.35229 | -48.16143 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd58fe8c-d0bf-31cc-9cd5-492cde97e4c4 | -10.65342 | -46.33873 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 993e1474-2e73-3fd9-8f25-ec35b5da1bb9 | -6.17784 | -44.62644 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 575998cc-c5f7-3441-b429-c2070c68c709 | -7.72302 | -46.31882 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 122a18d9-984b-3ffa-92c7-8878ff136ace | -5.64351 | -43.91697 | 2025-10-05 05:14:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3b319eb7-3297-3d98-8c37-a6a7525f267b | -12.45185 | -44.64095 | 2025-10-05 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45b726ab-ad2f-3926-820f-b170b671a661 | -6.73807 | -48.17496 | 2025-10-05 05:14:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49a93592-9ad6-30ba-91e6-6b03c4694a44 | -11.14616 | -47.92107 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91909749-1018-3eb1-828d-1a19d4f02fce | -11.0274 | -50.7029 | 2025-10-05 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2dfe4357-d49d-3155-bc86-3aea342d208b | -9.15774 | -58.30901 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4d4acc2-b437-3aa5-bbc0-96dc0ddada9d | -11.53143 | -47.23423 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a822aa9f-d79a-3a07-ac65-09bd0d0b0723 | -9.57007 | -62.26414 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6132c34a-f098-34ff-8ee3-3818baee879d | -11.02327 | -50.69684 | 2025-10-05 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f162a6dc-2e16-36a3-aa9c-3067bf0c59e6 | -9.10218 | -61.52787 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82427826-1d3d-3e7b-a22b-3eea252dc59e | -6.02257 | -44.02025 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c9cb8fd-8cab-35fe-b488-3650f76630c5 | -9.21928 | -62.47 | 2025-10-05 05:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5942a610-026d-3ca5-b9ba-ca11790e12cc | -5.60771 | -51.80495 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ecd6c5d-7756-3633-861c-58eb816d6156 | -9.84444 | -59.46766 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 852347f4-32c3-3685-b465-73b2e924888e | -10.04573 | -49.20584 | 2025-10-05 05:14:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 721a4fac-4e00-3b3b-90b0-4e4933a65e5e | -9.85416 | -59.83657 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README117.md)
