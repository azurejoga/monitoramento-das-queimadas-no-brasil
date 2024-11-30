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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0025fca-a40d-32d9-8ba1-6fc9983d58aa | -3.12968 | -46.05234 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9522304-9676-32c4-91da-37e84b73ce4e | -3.58581 | -53.46786 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3baf6f6f-a176-30eb-a569-882a3e9408ec | -3.06108 | -53.67908 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d2c9c6e-a614-3c24-87f4-558ed0304e6f | -3.60866 | -49.98854 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6de2c244-b5a6-379c-b385-a2eaf1991b02 | -3.09603 | -54.12985 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 638de67d-4f24-30f8-ad04-ecca1c36a17b | -2.90032 | -54.7738 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd9be650-31d4-36a1-a3e8-8f6eb5276f61 | -3.39691 | -50.31595 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 16386ded-8829-3ac3-b28e-ef9beb420c9e | -3.48781 | -53.98466 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fc2de36-1e53-398c-a439-695552f8a8fe | -2.61478 | -54.00812 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0678d78-fe8f-3458-8127-83955740a5ea | -1.42342 | -55.25719 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c4879b2-b62d-3e88-b119-61a618c4e511 | -2.77515 | -54.04786 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06837a2d-ddd2-3e26-ac20-510c7d0c8d4b | -1.12994 | -53.43023 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f386a82e-8515-3987-8104-7ca2f2647073 | -2.14441 | -50.62169 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 433445cf-4719-3c79-86e8-45680326e22e | -3.08256 | -53.76273 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55b9b5b5-3975-3f4a-b7f1-4a7c28cc3f70 | -3.21723 | -54.17714 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0088419-4213-3492-8cf6-15a8a2d6eac4 | -3.98958 | -41.5042 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b8dde6d0-9ede-3875-b0f6-07bf74d812a0 | -3.2182 | -53.83139 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50b945b6-cd7d-352c-bf31-087150778ada | -2.23396 | -54.92376 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb255159-727b-350e-bc72-ceac9f65bc3f | -1.40665 | -51.58941 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6000d2df-745a-3b9d-9df5-82701e52517b | -3.15429 | -50.62489 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 266b53ef-5d2d-3671-b590-a4a915e8a369 | 0.73629 | -50.86964 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d94ea922-8a23-30d0-a35b-220d6debcc0b | -1.31808 | -51.73369 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f01ab8da-af99-3394-a74b-51c3afb16977 | -1.32127 | -52.79281 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54e7adcd-be59-37fc-bc9b-dbb07b19edd4 | -3.08294 | -53.29162 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0b3dbd3-e131-369d-b1ce-7c875f38f197 | -2.88881 | -53.96837 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98358cd7-997e-38c1-87d5-b77dd18cba58 | -1.19334 | -54.01221 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 437cd69a-59cc-34cf-8d73-3ba452488098 | -2.84543 | -54.02631 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9a08860-39e5-3bd1-9a41-87c440eebd20 | -3.02568 | -53.41297 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf14d5c7-06bd-3673-bcd0-148401c77704 | -3.16059 | -53.23929 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9fd72216-af2e-3258-9c13-8d02a20ee6d8 | 0.93237 | -50.74269 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d079512-ed67-3981-9a81-0920bfc258e6 | -3.22501 | -54.17117 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0abf76c-4a0c-313a-9a8a-f706bc232268 | -2.85157 | -54.03085 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3de26e8e-1e40-36de-a2fe-c4f19e5b2a5c | -1.14311 | -53.66248 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ab55ea2-d728-3173-b290-c31a9f0815fb | -0.99139 | -51.72327 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45e424c3-264f-3fcf-a0d8-a913add69a23 | -2.7114 | -46.1263 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24968cfa-20d4-3a01-9ae1-bb423f62431e | -1.10438 | -53.592 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53fc7bd8-867f-33e2-ba66-af170ad17798 | -1.07172 | -53.385 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b877638-ed3c-3c00-acc5-a7c53f914f8a | -2.27562 | -47.89935 | 2024-11-30 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ad66476-c5f4-306b-8e8d-29108964a579 | -3.43232 | -54.12033 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3929ccf0-5555-36c5-a6de-1a397dc1b72c | -1.24434 | -51.62829 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b1b49ba-dc64-31eb-8c5f-6f1c67cc5a16 | -1.66126 | -55.23072 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf8ded80-a92e-3827-aa71-f1f4359ec632 | -1.41089 | -51.58587 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95866d3e-85ff-34bc-9f26-3664a06c71cb | -0.5783 | -51.69208 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aa66b58-068a-3541-bdbe-5d086dece88c | -2.11867 | -50.59634 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64284b7d-f9f7-3ff7-8e31-b3762e4ed19d | 1.86106 | -55.77418 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 668d6c3b-cbf1-3760-acb8-a37f5b3a52b6 | -2.84771 | -53.03043 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72b9b3c9-6e42-3f4b-bbd0-a5581183a873 | -0.90941 | -52.41176 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbc23e05-5021-3ca8-a1aa-17edc353bcf0 | 0.94265 | -50.73674 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca038d33-43c6-3496-b754-22f80b330147 | -1.42713 | -54.76202 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bb1f9f7-a44b-3af0-b1a6-2924f54a8b52 | -0.23425 | -53.75978 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e086cc9-c6b8-36b8-8002-2fab0e915c25 | -2.92704 | -54.32821 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09d914b4-9d9b-32d7-a296-5e729cf960ea | -3.78705 | -52.40799 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 453b01f7-95ba-3e4d-a23c-99940abc010e | -2.98876 | -53.35575 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b186cd83-f69f-3e08-9475-e70c622d1c9d | -2.66737 | -46.5993 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8deb1d0d-ad20-3f9b-be1b-eeff1a016c5f | -4.18442 | -54.76214 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f819cd15-2c35-3593-9985-704d6e540b89 | -2.92109 | -54.17046 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfa949d1-45e3-3d4f-ad78-ce3979843090 | -2.61495 | -54.0725 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3937fce1-fa03-36df-b802-005466edead9 | -2.72542 | -53.18832 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ad2f6a-d63f-3142-9c93-e667cb3260db | -1.46307 | -52.69325 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6829e739-ed6b-3cf6-813f-40cd218eee93 | -0.24701 | -53.7653 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52f9dc9e-d6ac-30a3-bfd4-9ac6e7b45163 | -1.72215 | -52.49107 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95a36d77-145d-3b1c-aa47-a02f2df5b4f8 | -2.97629 | -53.9277 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3050e5a2-5833-3c14-89f1-cd08ccde7227 | -1.11513 | -53.60069 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cfb2c97a-ec9a-3784-a96c-1034c38e3b0d | -2.78564 | -53.20523 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 809162a5-b72c-3b47-b59d-48e3be7d0c0f | -2.33333 | -49.09488 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc9de8a6-b0e7-3ef0-9b49-ba726c0d6d0b | -3.19606 | -46.57393 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaad2582-2c4d-3ba8-ba30-587c6f9fd4e1 | -3.25063 | -53.62474 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 6adf5733-9937-3d05-ad5e-074076e3fbf1 | -2.76681 | -54.05732 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f74be591-b1cd-3705-9332-ab7801186480 | -3.49869 | -53.82666 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cb8f4f6-8155-3ffa-84f0-3807c8128ec3 | -2.60656 | -54.27801 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c9822d2-2682-3fa4-a93b-85b68e72e9b6 | -1.10659 | -53.57801 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2a82c9b-7d2a-34bd-9dbc-c1d7234d9d93 | -3.41636 | -50.42725 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db33535e-5759-38ca-9054-37e2ebbfbd6f | -3.11339 | -53.76397 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 588fcd1a-c316-3a76-8dae-fc3761241352 | -3.25208 | -53.86547 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b570f03-a736-37a0-b83f-eee37a64a704 | -2.82801 | -48.47478 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0e4fb0d-a660-3f49-9d77-c0287078b92b | -3.11082 | -53.97717 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7ff2470-85e3-3a80-979a-68900e92736e | -3.0043 | -53.23489 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8a3f468-aacf-3bd3-ad76-88369cfd5848 | -2.54005 | -54.05746 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d16ef99b-fe01-3aec-b0b6-d7e261e76536 | -1.25805 | -51.63457 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6653858c-7759-3194-85f8-44f507127fc8 | -3.10781 | -53.3322 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d681dde-33c1-3f6a-a970-e5176510b554 | -2.1541 | -46.49017 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a344ca9-c8d0-300f-8d85-4d513f64b266 | -1.06232 | -51.75879 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2279e24c-3a2a-3d62-a636-1de937c152c5 | 0.09315 | -51.16933 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5101fcca-7ada-3be9-a71d-ab00de55fad6 | -3.49643 | -53.81902 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ca52980-d635-3e12-861f-5db56f3081da | -1.40536 | -54.51182 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13e0580c-61b5-3e1b-ab1b-65955d0e7029 | -2.56801 | -51.83735 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df29c4f9-ea26-3b92-8624-fab0919c5805 | -2.30445 | -46.54348 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0ea91c4-3a4c-3f6b-bedb-fce3f682ced9 | -2.98196 | -53.3547 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6146592b-2c47-3640-83b8-8e9e53992b9d | -3.86196 | -50.54051 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82d51b94-2325-3482-bf69-fbd36f700c36 | -4.23734 | -48.08561 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13823d53-50fa-3680-ab7e-e33b98787709 | -3.7665 | -50.17557 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 073a2911-4f85-3b5d-bc77-c2733fb3b619 | -1.18505 | -54.02161 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba639119-a8e9-3012-b45b-d59ab8793296 | -3.78329 | -46.69384 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f438120f-5e09-3b7e-8762-7d8d9ec9aea4 | -1.33174 | -54.61684 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 674a1f61-25c1-3a64-8098-9cdb20532738 | -2.62606 | -54.06709 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5caac4a-dc08-3508-9fa1-d2e943a45534 | -2.59864 | -54.21989 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bebd9c6-cd93-3598-970c-8905551a80f4 | -1.71595 | -52.63184 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9c4fe9f1-eb55-39c4-b1cf-1bdeb73bc1c0 | -2.78476 | -51.71574 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ad5dfb7-4f17-3241-83a9-303bb26f471b | -2.13825 | -51.41446 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25f08bfb-e5cb-3056-85d3-71883a875120 | -2.82309 | -51.95237 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README102.md)
