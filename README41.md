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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efbca3da-3ab2-31fa-a10a-1bdd13999a0d | -1.31215 | -51.73776 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8103e357-085a-3748-8b6a-f4653b6c2870 | -2.33966 | -52.17845 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22532607-5043-3461-9a98-76efe6385cf7 | -2.32151 | -51.31071 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a47bb67-4698-3882-a0fe-5984a8f680f3 | -1.77389 | -53.62566 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a196ab6-0828-3453-96dd-4b0936db1519 | -3.28526 | -53.67798 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4aaf0720-89fa-3b5f-906a-27d9d1b81087 | -2.2207 | -46.38886 | 2024-11-25 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df2298eb-b21d-3dc8-bf24-fa7a5a109e26 | -0.96171 | -51.78218 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94539a4c-4e27-3ae4-ae52-f67a9ba2c5d9 | -2.76636 | -54.03015 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a460feb9-7ea6-3965-8bca-e08175d5958c | -0.81867 | -51.6112 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e221d36e-681c-3b11-a2e7-0a4251107a21 | -3.66357 | -54.58801 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8ce3c52-22f3-364b-a9cb-96a92407246f | -0.79959 | -51.60097 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bca34ede-b88e-389b-b047-d8b8b1b59498 | -3.20111 | -51.60106 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8e75cbe-5770-33dd-84fc-2dc03f668aaa | -1.49269 | -52.44706 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b08f8782-9eaa-33d9-bad7-f885868f5cbc | -5.5838 | -45.20713 | 2024-11-25 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cfca6e6-8741-3d01-80d4-a5b975d1bbc1 | -1.35108 | -54.6362 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d1761f1-8af6-3c76-889d-d6c65a1bd46e | -3.40623 | -49.56398 | 2024-11-25 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 34fcecc8-cebc-336b-a30d-e958310e5942 | -1.77358 | -52.72828 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6fda22f3-7d71-37c6-9ef0-b8f67b7f0257 | -2.61021 | -53.96665 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d4d23a4-1ff2-30bf-ac98-4bfeef099a00 | -2.81602 | -54.71558 | 2024-11-25 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00ac8c46-fc04-3f99-8100-5d0681b8e9dc | -4.84449 | -50.80569 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94443642-301d-32ed-b748-7d6fed4e26a4 | -1.19668 | -51.76374 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 554994cf-675b-360d-a9e8-ae059ef5bacc | -3.29058 | -53.8382 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd2ffaf9-5604-3079-9bda-98c26ebc2f8e | -1.77913 | -52.73621 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c62d02d4-7a63-3683-b60a-c502c3c6e6b8 | -1.22519 | -51.73552 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5305d5d6-4afb-39f7-b994-cc1f3bfc1ccf | -0.34301 | -51.54169 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ffcf355-4277-3a07-91ad-4ee1cb11fea6 | -3.222 | -53.93061 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c6cd4e-6182-3515-8041-938aa9247b08 | -2.02407 | -51.18335 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0b0bc27-8a56-3c83-9f17-1a63002866e0 | -2.01208 | -51.1701 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fc3649e-d937-30ce-9e6f-6539e2af76e4 | -2.92742 | -51.76874 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa72bfd-cfec-3fb0-ada5-a1f1a420248b | -1.43838 | -52.44572 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03e7d732-b207-32e2-b6f9-df39a2ca3505 | -1.67126 | -54.97271 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a19a866d-fb82-3c03-9436-b82b4d770a33 | -1.69789 | -52.60626 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aee3808-e66c-3632-bb3f-8405d99876ab | -3.03406 | -54.06876 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b071e472-6536-3d6e-a3d5-d9e73c5ad818 | -1.20506 | -51.75416 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cba5d61-bf0b-3974-957b-1e97d1aec009 | -3.02737 | -54.0463 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b4b1df-7336-35c6-82e5-244eefb9a52c | -2.17735 | -53.77065 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a48cc8ee-410f-34e7-898c-bf176e4b319c | -2.76306 | -54.05107 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca3cf5d3-15d1-3c3c-9414-4c09d2e7c2c1 | -4.96772 | -50.04517 | 2024-11-25 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e63eb3c-d317-324c-89eb-e5883c99c224 | -3.94243 | -50.46519 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61696815-271d-3175-9067-5174965ce398 | -3.06259 | -53.28656 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7a774f8-5637-3ba0-9986-8d8b8288faac | -4.2477 | -47.98478 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e6a9299-7a87-3f88-8e4f-e0377c71d3d4 | -2.32553 | -53.75446 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5ff5d5d-e8b2-34f1-a22b-3b6f7fa00b89 | -1.12109 | -53.73025 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a235bc30-7613-39e3-aa4d-e6fb7691abdc | -3.2996 | -45.67952 | 2024-11-25 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c3dfc100-35c3-3eeb-a931-2e43b47329d1 | -2.92402 | -51.76824 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46334054-e16f-3ea5-b0bc-7e26abbc970c | -0.76244 | -51.77261 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 317ba54b-f406-3999-b1a1-57ffbf48cb95 | -3.3482 | -50.50666 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b9518452-649d-315e-a43c-2897d29fc9dd | -1.12997 | -54.17552 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ea7c5e5-ac0d-389f-a3f2-b942c3c0e82a | -1.10535 | -52.34761 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab895021-654d-310f-9ce8-c4be3d8572da | -4.31201 | -45.89453 | 2024-11-25 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54e81cdb-0ab3-3582-aff2-d9f995b754f4 | -1.65668 | -52.52193 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cc4cb87-38e6-3716-b2b4-bfc3e239a50c | -2.79946 | -54.11754 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff5032bf-f69d-30ea-bf2a-f932775b4344 | -3.24175 | -53.63231 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 966fda00-c0ce-396e-9383-8406bd0c284e | -3.40247 | -49.5634 | 2024-11-25 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2051025-b835-3247-ad0f-80f363f1cd8b | -2.58414 | -54.04484 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc822e7a-1c91-3e58-ab1b-221208031c27 | -2.82113 | -54.08871 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 759b25e6-dff0-3735-92c5-6a5b06c6df15 | -3.24907 | -53.28371 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c27085-92aa-3f66-aea8-4f45ec49065f | -3.64937 | -51.38688 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f34e1ca-535e-3608-8401-24e55b738235 | -2.56446 | -54.00238 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7e66ae6-92ab-3553-a154-f53447916a0e | -1.59926 | -52.2644 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a71a586-c0c4-347b-9854-43b2b20177a9 | -0.39058 | -51.44707 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7477c3d4-b3be-3b0e-941d-071c27da937f | -3.27669 | -53.81833 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| def517b5-b305-3dc4-996f-e950bcee34a8 | -2.66975 | -46.60496 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b53c6ca7-7bdf-3c77-ba51-4a57cbb98d6a | -1.61752 | -52.57608 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae00c0f9-9065-397b-bd5d-c5468fdb4b2b | -1.59647 | -52.26041 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 394c1b90-d043-31d7-9f2a-3271974ac929 | -3.52229 | -52.74815 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2019f0a1-e4f2-3c77-8576-4059228f7833 | -2.8466 | -54.01408 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e6fd5b5-f23d-35df-9eb7-b82a36962bac | -2.78509 | -52.87899 | 2024-11-25 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1374d821-b792-35c6-bfea-e82494eded01 | -3.89168 | -50.07096 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99311143-2717-3023-8c9e-a29981e9c405 | -3.27042 | -52.95821 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 102cc842-7fe8-3aa5-bf54-c753104a23bc | -1.43428 | -53.37747 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef96a390-369d-384c-bab0-54583fad116f | -1.4288 | -51.1233 | 2024-11-25 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d075d2e4-1702-37e6-af3f-bd0158eabdde | -1.44154 | -52.57727 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2957d4e1-f84a-3033-8a04-5ddc05d5d61c | -1.47868 | -51.95935 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5548b57d-7866-3a4c-bd21-cad59393c1b5 | -3.10089 | -51.50333 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 152fc1db-1c17-3618-8175-6af5197e3468 | -1.40884 | -54.46784 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6a4f6d7-a51e-34f5-a75e-8d7cead583b7 | -2.90177 | -51.77259 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fab1b85-7003-3a54-b487-c0f93fbf1ada | 0.80525 | -52.01793 | 2024-11-25 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3065d00c-ba37-3088-81ae-f3a830115bbb | -1.13657 | -51.67472 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 274e2045-7d41-36b8-bfc9-215fc483b14a | -1.44709 | -53.40425 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b766085-b796-351e-b28a-973181c17220 | -2.82717 | -54.02889 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7404fa6a-0b75-33dd-a10b-29a1769f0b54 | -3.23142 | -53.93202 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcd3a3d5-ad31-3c05-a80e-b4c8ffad2a72 | -0.0344 | -49.63917 | 2024-11-25 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4994fdbe-7b9d-3334-97d2-8fced12736f4 | -5.58425 | -45.20399 | 2024-11-25 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86e3ec42-36db-3f6a-97d2-9ff28a8842d7 | -3.68409 | -54.55474 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0648d535-4442-3564-9dbe-642323f17543 | -3.24725 | -53.61903 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e51980d7-7e72-31c8-a7d8-8195d94bb406 | -4.24184 | -48.67071 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f414554-735f-3f41-aa4e-353d8a71a519 | -2.63468 | -53.9848 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01d0ef63-2625-3aa9-9cf4-0d2bd8f4c4d4 | -3.26617 | -53.82024 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d58a37-8b44-3c32-b2d4-06269d7ded34 | -3.63127 | -52.24636 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ef69369-2df1-344d-b855-0847a82aa1c6 | -1.13257 | -53.6144 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebb920a0-3116-3a7a-8a97-2def8cf1a596 | -2.33185 | -53.86578 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d1bfc2ca-9f11-3289-91af-26a6679ad8be | -0.75734 | -51.73934 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1720d4f6-c4c3-3541-a943-a995b18590c0 | -4.97554 | -50.74931 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb544fbe-6ec4-3663-816c-8d615b3faf6e | -3.07309 | -53.28466 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cc323a7-3332-3d5e-8300-b220d13521bc | 1.94606 | -60.85461 | 2024-11-25 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7c94974-1811-3165-a90a-0a9300394fa2 | -2.80827 | -54.01878 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52f3d667-7b3f-3c99-ab0f-2e680ca5c6b4 | -2.83161 | -54.02244 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b712c27c-a77a-32c8-9383-7c72894e1158 | 1.04628 | -51.849 | 2024-11-25 04:55:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f41eb3f5-9f47-3ff2-9b75-cbe25c3d332f | -3.65727 | -53.46425 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README42.md)
