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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a134e4c-76ec-3f2d-a1c7-8447b0fca4ae | -2.89154 | -49.38124 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92a90576-1b06-393e-9197-eee49e230f7a | -4.01607 | -46.18211 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 881cf42d-bdb4-30ca-b80f-5bbb6d51f738 | -1.51507 | -52.17749 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db0f992d-c13b-342f-9f89-d9accf695beb | -3.76618 | -51.75851 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ba7351f-5713-3282-bd83-c4f6f496144c | -1.68192 | -53.18069 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04839a3a-849d-32e9-b24e-e940c4235a27 | -4.0873 | -48.51236 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 959ed278-0459-30d1-af90-1fcf56288d9f | -1.42604 | -53.40873 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2aba539-b1f9-3fd4-af9d-5326365cc047 | -6.27051 | -44.54299 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ab0bc0c-f296-36ba-8258-2dea9b652b85 | -2.95133 | -54.45932 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c693eb-253e-3537-bc60-3821c1a0069a | -2.72948 | -51.73579 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d2aa5a6e-8afb-3621-84b2-700ea215a3d2 | -2.41605 | -48.93424 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f555c08-2b95-36c4-8643-483778fb1502 | -2.19052 | -53.62801 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf53ca2-d292-3994-9c8d-04fbc52f295b | -3.88482 | -49.95033 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8979864b-f291-32e7-9703-073fafb3da34 | -1.05936 | -53.65309 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 859d2b23-51b7-36cd-b6e7-a1ca71c2df87 | -3.04828 | -50.36173 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a36851e-1194-31e4-a81b-56d4b55da6c9 | -1.12548 | -53.72441 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a29ef88-b64c-35e5-9910-022990359439 | -2.11308 | -50.847 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dd6c032-3b54-3945-ac44-5c070eefe6ae | -0.5649 | -51.73634 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1612ffa6-6132-360a-9766-97538550243e | -4.78316 | -48.67903 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 375d7b12-6497-3ba7-9cf3-ede88aee7642 | -2.07268 | -48.51365 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dde49ed-1e25-3a06-b7f1-d3ac9bd5be4c | -3.16012 | -54.47757 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f71c118-46a0-3363-9e0c-6a2d577b3e8b | -3.47869 | -50.80119 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6367c89-3b8c-328e-b134-35990dbdd43e | -5.0397 | -45.8714 | 2024-11-09 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5a866e6-b70d-3ba3-86a1-62291f7af616 | -3.01515 | -53.87085 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1aadcdec-3eb6-36e6-bbb1-acc06691cbc4 | -2.84472 | -49.51057 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ff723a-1a55-3cca-b42e-c07f20f9cd50 | -1.36591 | -49.35009 | 2024-11-09 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b4ae286-b1b8-3ff9-99c9-cadcd0d96d2e | -3.10705 | -53.71472 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a3d1e3f-ae8f-3c93-8ceb-da25b001514c | -3.58337 | -50.26896 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a13f1e12-36e4-363f-b9ca-49dcd019b282 | -2.83813 | -52.9094 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e353d59-6b77-312a-900a-3d4a7fa4ec36 | -3.95814 | -48.12883 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26f2b212-ffea-3793-abe1-f6d38fde9d50 | -3.54471 | -43.56808 | 2024-11-09 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5be1d078-cc99-3bc7-92f2-4802d36f7777 | -4.39674 | -47.64729 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d21f6412-148e-34a3-813d-c44a525197cb | 0.03125 | -49.44915 | 2024-11-09 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6155cee6-6f08-3305-aa8c-3a87cdab3f6f | -1.35867 | -47.3196 | 2024-11-09 04:55:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7c27660-d52e-318e-b0a2-87c463eaa787 | -3.05148 | -51.14129 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9474e507-36f0-3130-ba40-255bbc6e69a5 | -2.3334 | -52.76352 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cb533361-7e86-3414-a19f-d17afd294858 | -3.60509 | -51.24259 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a257642-7a99-31e2-b59b-a14e1d00f4d8 | -4.84604 | -48.64752 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ea90b0b-df6e-3254-9eb2-854717ff723b | -3.32775 | -50.23658 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a79a5b1d-9426-33f5-9f0d-de7a76b396d6 | -2.68783 | -51.82205 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62ec4d88-f5d4-3e12-8c6b-2b3381ed08cb | -1.62346 | -52.24047 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c6f22be-9744-3042-8107-e0baa719bdda | -3.58631 | -47.34503 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccbe83f5-9a6d-33ca-b49a-2113dcacb70c | -0.89393 | -51.77656 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dea51203-c6e3-3703-ad67-aad03f826b5b | -4.2514 | -47.57249 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| f3d13868-83ec-36da-b065-b5998c66a3f4 | -3.18655 | -50.59241 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dc2e9bd-a7e8-39d1-a144-6ef0b8ceff05 | -2.94317 | -54.45845 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 556bf913-c45d-333d-bbf0-a031794eb075 | -3.92604 | -50.24545 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e1a5fb3-b22a-301a-9ee2-f9875fb0a024 | -3.97949 | -49.98971 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b95abc1-7cc9-3881-848f-972ad9cff67c | -3.45856 | -54.53519 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2eee825-b873-3bc8-9a79-ad1692862216 | -1.61195 | -52.65765 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d535ce17-ed35-3464-947b-59003680c61b | -3.0922 | -53.31695 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a96cdbaf-dc29-31c0-a3c8-ef3faf7242fc | -3.01464 | -53.44257 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ed307df-3149-3597-b1a5-9062d6156378 | -3.64631 | -50.1734 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16c53fbb-fd20-3008-a0ae-67bf28645564 | -2.81671 | -52.95909 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 316ca2d6-1e56-30f4-b1ee-f86b101e9d6a | -2.41112 | -48.5201 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 3ef1ac01-6303-3d59-a17f-b09463cfc6fc | -3.65514 | -50.13995 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f08ef70b-1540-305c-a7b7-6b404b5a400c | -2.5824 | -49.14006 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8073bddc-2994-3990-aaca-9fa1432c14b7 | -2.15637 | -50.91216 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a1e157-0005-3e47-b05a-ff0a77869290 | -2.86142 | -48.44983 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbef3d7d-9004-3583-83be-2d5cc32cace3 | -5.43814 | -43.2553 | 2024-11-09 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e801284-bf97-34ce-9212-618ed45ed1be | -3.23277 | -50.27042 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 437c43ec-b1f3-380c-b9f8-8d1aafe2da0c | -3.96699 | -48.12651 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be3135ba-9ed7-316e-9d88-7897cf08f91e | -1.70059 | -51.08244 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a87e0752-a430-3439-b201-acddc2b4e91f | -0.8149 | -53.05552 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b2266a3-2995-3e76-94b8-0ac32470d13a | -2.62487 | -51.91494 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df57f8a4-eca3-3208-b38b-3bf0314288b9 | -2.22557 | -46.54874 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce5f5bb7-000f-3f44-84a8-e66f030df904 | 0.84671 | -50.20879 | 2024-11-09 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcab9210-fcc8-3b31-a24a-afa209b11494 | -2.57191 | -48.25694 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08d0da12-6215-3124-a65c-a376558e84cc | -2.45822 | -53.68718 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e9a0fe1a-3ea8-3b73-bf55-327a0d6b1b3a | -4.24138 | -48.01855 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70b79207-d2d9-338a-b5b4-c199b2d2f210 | -4.80087 | -44.77928 | 2024-11-09 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a74c57fe-fbde-38cb-9a65-f9d78d63e69b | -4.3804 | -48.15558 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11b2ef80-45f7-3742-9587-4ca5ed205c80 | -2.62078 | -46.16051 | 2024-11-09 04:55:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0933fca2-5193-3eec-8674-6407306ea7ee | -1.46204 | -53.41791 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ad5b648-00c7-336e-b8d2-5243f35b8ce7 | -2.11529 | -50.15013 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63f16650-aa7f-3876-b8d3-03246da77fd3 | -2.40894 | -50.3035 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ae26f86-c05f-3b2d-bb31-df2073194c4f | -3.02801 | -51.00991 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b21a27eb-0a0a-367b-8e62-37cc576ea827 | -2.08512 | -46.52078 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92e0eac6-3c77-3fb6-8ef8-b58ef6c72b1b | -2.91393 | -49.36129 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b35a6ca-af98-312b-a55d-3cc34fc6edb8 | -4.60323 | -49.57964 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3b4a83b6-492f-3770-889f-d8029618db03 | -2.71895 | -51.71245 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d949881d-c251-3f30-921c-3baf48c32c53 | -4.4127 | -45.93794 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ce1b08b-1737-3029-84cd-08025d1e47a1 | -2.69689 | -51.69792 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02d5a718-d418-3627-b986-f7419934b981 | -3.40073 | -53.80649 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7e8b88-ef08-36ae-a222-6642ed45baf7 | -2.88142 | -48.29236 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5831cb12-3422-36b7-b656-2d384aec9914 | -1.72854 | -52.3708 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9a4bdb7-4f4c-3ab3-ac0f-82db9246d21a | -2.60457 | -54.02357 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 305198a5-7390-385f-bc05-9d0aef1bdab6 | -2.22034 | -50.89771 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4113a55c-2d8d-3f3e-b34a-495401b69d12 | -3.29223 | -53.24911 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ec0600-1a2b-3287-83b2-ef21fb52b886 | -3.65101 | -50.75624 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b65c869-913d-3929-a0bb-fce8b56bf478 | -2.46664 | -50.40307 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bba035ee-477c-39e2-9703-94f698d643b1 | -3.11927 | -53.12335 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cda4622d-110f-3e8c-bffb-dbaa4ef51862 | -2.92289 | -54.19545 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b677a81-907e-3b40-97ab-bb4b531ac590 | -1.19992 | -53.70749 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34fa0f90-4e5e-3684-8453-beb48a2e9d32 | -2.11592 | -50.14604 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbaab13f-f19e-32c4-9b6c-208d14fa6fda | -3.03741 | -50.37317 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca08919-9eda-326a-ad26-4d317da3a65f | -4.37202 | -48.15456 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3f81a7d-0c81-3224-9749-332be931ef12 | -2.45435 | -53.69013 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2c5dfe4-f5b1-3900-ad74-f22654c266da | -2.40475 | -50.30699 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a53fec70-5571-3dc7-8d3c-82db917d22cd | -2.44785 | -49.60945 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README81.md)
