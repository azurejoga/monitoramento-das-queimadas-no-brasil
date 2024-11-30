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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cc60d5a-c7c2-3af1-8a9d-e5da72d3589f | -1.88018 | -48.54463 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a95eb29-635d-30ad-b60d-479b0ccc1cf4 | -2.10804 | -46.56583 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6885b581-9ecd-342a-808c-61856da5ccd4 | -1.78501 | -52.7486 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a4699c9-be37-35ff-b43d-79250d2fc9a9 | -4.8803 | -41.28999 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 0893dc46-7d64-319a-8395-273fc1a90595 | -1.75812 | -50.85538 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ccaf3cc-e624-3d72-a3cc-29583867a939 | -3.05843 | -48.51445 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77db2c0a-8df6-3adf-8735-6d0e87de1dba | -3.71933 | -47.14994 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84226852-308b-3ed3-9634-7942811b4634 | -3.10229 | -50.36685 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae578ec0-eb7c-33ce-8188-dbd52b33a803 | -2.76378 | -49.22478 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1d388d5-2b59-3952-a11c-f739986a2f06 | -2.60982 | -49.2538 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8b7c546-e868-33cc-9f9d-cb2912098da7 | -3.09837 | -50.34792 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 53e6839b-9eaf-3d13-8d70-362d9ba804c9 | -2.72945 | -48.90285 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44fb7f7a-a12c-3df7-9378-4409c53d6c3b | -1.32334 | -51.67402 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a11d1f2-227c-3811-8fad-147b7faf6032 | -2.18481 | -50.29056 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfe4fa54-ea21-3246-89cb-9880b3dc18b7 | -3.35345 | -50.51628 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be8b17fb-dfd3-39b8-b025-eb8120636401 | -1.92159 | -50.55616 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 900a2ac1-70d2-3629-96dd-c5d0a5ed8657 | -3.78648 | -52.40509 | 2024-11-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c7ddfd6-e126-38fc-abba-6497c8bbe1bf | -2.26906 | -50.4896 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2f44c11-7512-3016-b90c-91c928c5b446 | -3.75671 | -49.94504 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88c9b428-59a1-3514-822e-ee231438f549 | -3.30302 | -50.49697 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe8da95c-7ae7-3710-84f2-88e70c330dff | -3.69599 | -47.14242 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 229efa95-f047-3a0a-b0ba-5f6d162ca179 | -2.03168 | -52.07675 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d15b46e1-7072-3a24-808e-c31cab537907 | -3.1833 | -50.2807 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b45e2ab-e32c-34a0-ae67-cab3dd9091a3 | -1.2725 | -54.5594 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86e4f59f-dc90-3698-9112-7b052a9ba9d3 | -5.91489 | -43.83821 | 2024-11-30 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d4830ec-06b9-3fe0-a486-71648356f536 | -4.87275 | -41.27203 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 4541f1a7-359e-36b6-85f2-97b060fe2a6e | -2.69089 | -48.62612 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d48095be-d0e5-3e86-91b7-e4d391dfba43 | -3.17913 | -54.32504 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc1dc329-ecf8-3ecb-9374-fd25a47fe169 | -2.7117 | -46.12171 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3f70cb7-78a3-3558-b5d0-4b02e6ecd995 | -0.88875 | -51.71798 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65e49d0d-5387-3cd1-9dbb-fbdd14a63669 | -0.79735 | -53.05916 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5590ac72-428c-3b83-a0db-30811fc1088f | -2.81129 | -48.61662 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60c5bce9-1d84-3498-ab97-37503c5bbfdd | -3.3051 | -51.06466 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a91a999-89da-326b-8d18-3ad1c5d172ed | -3.74239 | -54.67922 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4390f7cc-2ad1-3f5d-a22d-89fdd3944cb1 | -3.20398 | -50.21486 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a796361-75af-3a01-af3f-5fa0086f7323 | -3.3571 | -49.76065 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d549f69a-8fa9-3266-a140-dd5d90cdffb2 | -3.34669 | -50.51525 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0aa619c-b1e9-31b7-88ed-4f4fe27dd3a8 | -2.71382 | -46.20286 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b3a421-0319-36cb-bcbc-b0f8ee3407d1 | -3.11136 | -53.27248 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00a9a89d-9fea-30ee-a46f-73295d53d975 | -1.28241 | -51.66471 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c8e8970-cc19-35a8-8b67-e8c650681c63 | -2.7231 | -46.23646 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4af7b99b-69ee-3d5e-9a65-beaa7e55d02b | -5.04722 | -43.62186 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59834503-dc1d-36a2-914b-96d8b0ae0565 | -1.05004 | -51.81419 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cd9148c-f7f5-3a85-9948-ae7b99a8d157 | -4.15415 | -47.85415 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c203ba-8655-359e-a27a-224574569ef9 | -3.30977 | -50.498 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bcc02d0-d93e-3a88-b998-1f34b68082ce | -3.27988 | -50.5783 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cbd2e29-1332-3869-bbe5-b15e27c57aa6 | -3.32933 | -50.21957 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f95d50f5-bad1-3cc1-ae8f-5d0ef1ec0cce | -3.27909 | -50.19004 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63df6c80-3c38-3196-bd16-1ae2cbc42379 | -2.70653 | -48.67776 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d6baf4a-0c1d-3cfa-87f5-fcff56fd572b | -4.0427 | -48.33076 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 149a3962-ee99-3fe5-9c6d-b024d6902991 | -2.8467 | -54.08453 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2732dc90-1f89-362f-aa92-ab379f0fd4e7 | -2.9162 | -50.31938 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d40bfbab-142e-3d63-9007-72a02c9856c0 | -3.95108 | -46.92054 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee326112-b5c7-3f9b-985e-8890543d9bd2 | -2.82288 | -54.10298 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68416336-49f4-3ed5-9198-e653d151ff74 | -3.05826 | -49.54036 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87e752fd-efc7-3ba8-9746-1d90c0fe0b90 | -3.93512 | -46.50415 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fd95068-04a3-3177-8425-beee2ef3c7e2 | -3.7436 | -50.26663 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4cd3877-858b-329d-8ff7-5a9d7e4249fb | -1.58498 | -51.25932 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dbe692a-fd08-37af-907e-cf16d712f1ef | -3.19928 | -51.41801 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cff6790-aa08-3471-8a47-61ba049eac75 | -2.82055 | -51.78944 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf8c8a90-9905-3449-b693-c6beb9c2c636 | -2.02724 | -51.19344 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c35baa0-9a3c-3855-95b0-2f69d40e9a34 | -2.86437 | -53.99911 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6bb011c4-8e01-3fa9-a85f-499b17cdcadf | -6.93045 | -45.20464 | 2024-11-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4843907-1831-3ac9-8819-91534b0c57e8 | -2.70432 | -46.12177 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69d4f539-f674-3059-903c-fadcf8edfeef | -2.67459 | -46.26611 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 014db85f-ebab-387a-ae3b-ea5261bc442d | -3.25486 | -53.86075 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 042ee3aa-a783-3757-9a49-0ee3896bdd31 | -3.68762 | -45.68028 | 2024-11-30 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e17c121b-4b20-311c-9967-16aeb25c3e89 | -4.87692 | -41.27829 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d50b1754-f224-382b-8000-76c7b0a0daca | -2.30057 | -46.54895 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c515ad5c-de8f-33b8-bf30-c8cffc47ab20 | -0.96206 | -51.65219 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ddce777-4fab-3e0e-9bd6-2a70fc0f054b | -2.23482 | -53.62931 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e677065-95f6-3e12-8bcc-69437dda6e59 | -3.81462 | -50.95247 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b918451d-b492-38d2-aebc-3971c037fa0a | -3.27802 | -45.56711 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dbfda390-5dbe-3dd6-9a93-a2eeb7d3de1b | -1.51023 | -45.89999 | 2024-11-30 04:40:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c1779fb-ad8f-3387-ad5f-a28435cfcf1f | -3.95454 | -46.92104 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6164c020-cc73-328d-9c1c-4590d00c92fd | -1.57845 | -47.86273 | 2024-11-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcd053d7-6128-33e2-95a0-02613d9e4848 | -2.67043 | -49.86462 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aed2f46d-2ec5-3a90-bef9-8ed92fddbf2b | -2.71304 | -48.65766 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e36a8ed0-b3cf-326c-ac56-c6ad39391159 | -1.58913 | -51.25593 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a6869ce-6f40-3c89-a589-6355cabd9633 | -2.45852 | -46.56781 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8adbef44-49be-3d7c-bd51-f5b90416eef3 | -3.31258 | -50.28242 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5974a8f-a521-33f8-9d46-33418eba07e9 | -4.35721 | -50.86881 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64b7e0f6-5e63-3cb6-b691-80aec4aa8663 | -1.99823 | -47.39263 | 2024-11-30 04:40:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6af97436-d374-3b43-beb7-dd98bb0e96f5 | -1.96805 | -52.89535 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 343f5ac8-6f63-38d8-8c35-9d4e891cd69e | -1.53866 | -55.8647 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3d74ea9-811b-3e33-87b1-bdb45fa6767f | -4.11649 | -48.53432 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0912a29-b5d8-36c3-bfda-5d7f5f6e9b9d | -1.53282 | -52.70098 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62a38368-ffc4-3d40-acb1-8ac842730a7a | -2.26207 | -50.35841 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd32e196-8a4d-31ef-bd47-56120f83e576 | -3.09764 | -51.06718 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0366f863-3870-3977-9745-0d9322412c8b | -3.94309 | -40.97105 | 2024-11-30 04:40:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44d623b9-a727-350c-90c9-ea281b424d3a | -3.4068 | -50.66156 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0153332b-ee20-3c31-b502-fa23f6d2e6be | -1.73032 | -49.80796 | 2024-11-30 04:40:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78f31839-6ab6-3fe4-8fcd-cbfc36aaeb48 | -2.05969 | -47.56544 | 2024-11-30 04:40:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b16b651c-dbe3-3708-ab62-7470cb6d3925 | -3.24266 | -46.41611 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50068bb8-148a-3900-b6a1-74b68d07da41 | -3.74004 | -53.3927 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49887a42-670e-3751-b7fc-7fe610cdf77e | -4.16798 | -48.62018 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e42b7de-69e2-3637-b3d9-a5fbd2c7e70d | -2.71937 | -46.1188 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca658ccc-9fd3-3101-b55b-f0390e20d5e3 | -4.87277 | -41.30732 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fc53bdab-8272-3d2c-9c3e-c0f055cd8c07 | -3.49823 | -50.28975 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e82baf8a-9ec6-38e0-bab9-c9e6996b84de | -2.48334 | -48.84298 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README71.md)
