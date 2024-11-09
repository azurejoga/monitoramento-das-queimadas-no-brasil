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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6512c1ce-0452-3680-9f15-e4c6645b3587 | -1.14372 | -53.65234 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61bc0437-2942-3143-adc1-24e70835ad00 | -2.56633 | -54.0358 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82b29b07-3cf3-3d6f-b161-a6285cc11be7 | -2.48047 | -53.97897 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7329ae03-fff9-38c6-969e-8c42e59ca6fa | -2.15721 | -50.51243 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b142329-7659-3692-8449-a76ee3dfdc02 | -2.28628 | -50.67941 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b465545e-04a2-3971-9182-2cde427ba102 | -3.7529 | -54.64241 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 056f2d06-c3da-39fd-aef5-20067e24c1c0 | -3.52058 | -51.24954 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 273732a9-3856-3124-bc3e-1f1d1b1e8977 | -3.22359 | -50.63483 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e8dee24-db82-3b17-9db9-d9a89f577658 | -0.39123 | -51.94233 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61da01d3-4694-32f6-9567-b19d04112c00 | -1.16373 | -53.6554 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 989623b5-27f0-3963-a393-4d3213e9f5c2 | -2.49043 | -50.20346 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01591833-3b87-3343-b465-c7c09da41d00 | -3.48824 | -54.57599 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1019e8b-dd02-323b-bffe-6b7e94dd36fa | -3.35542 | -50.12922 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1110889-c602-3cd9-97e7-e97410e1d039 | -2.28046 | -50.67058 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8eb6dfe-06f0-3c82-8503-38364061a4bc | -3.27451 | -50.34303 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d467a80-aace-3fff-b775-4586df21dd48 | -3.0458 | -50.37805 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2814231-8db8-3afa-b67e-e0817d9abdf6 | -0.54428 | -51.79095 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c3e46ad-447b-3ea0-9bbd-49007ff4b722 | -5.25094 | -48.08661 | 2024-11-09 04:55:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27480bad-add0-33d4-96a6-cc0100be4d28 | -2.44993 | -53.69654 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4481958-9d71-3435-ac1c-7fc33b85636c | -2.83182 | -49.49483 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9b2939e-8f95-382f-a729-e22342ff9ff9 | -2.98288 | -50.29777 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 180fc3b8-ea9c-3ca6-a233-b85f1d56a451 | -4.12811 | -46.85405 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f474902e-30e4-3c10-8aa8-0730d4154671 | -3.29974 | -50.0791 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d83fb740-7839-305a-94d2-11ad3e4cdc1e | -0.97833 | -51.78603 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4f1ad6d-958b-30a4-a702-35f1359ad227 | -2.58178 | -53.98103 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 309074b2-f74b-360d-995d-954513a80da1 | -3.35626 | -53.78886 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d542573d-27e4-391b-880d-6361f10a41d5 | -3.11423 | -53.7123 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97b31b1f-db0d-302d-b53e-0ceb5beb029f | -3.13353 | -45.95573 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb730c5b-f37e-3f52-8461-45a7a9324c40 | -2.66522 | -49.86916 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeabb7ca-92f8-33dd-abbe-71ef5b90d26b | -2.64462 | -54.368 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aed0723a-eee1-3ddc-98c0-48ec2cbd65ff | -4.9398 | -48.24331 | 2024-11-09 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 069328a3-5ee2-35e2-938e-532c7464ec40 | -4.87428 | -45.77921 | 2024-11-09 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8b4247d-e72d-37f0-99f1-2c835851d711 | -3.12574 | -50.14497 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 413a370b-0e80-3d29-b314-5892736ff302 | -2.90377 | -51.46772 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e267dd88-69ef-3f61-8436-96b74d9d8594 | -1.3802 | -51.41222 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 447a78f3-3cfd-3052-8151-753005fd5c9e | -3.19803 | -53.41794 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cbffe3f-ebe8-3876-8df3-4d71844d2cb0 | -3.74162 | -50.45134 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1da421c5-fa66-33f6-b312-e64de6e5a77c | -3.73181 | -53.40281 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c3b4e8d-652f-39ba-b80e-46ea1bc7ed0a | -2.32747 | -49.69112 | 2024-11-09 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8afa6f8-87c9-3712-b7a7-8222f88007ad | -2.45768 | -53.69064 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7978be5-c384-3aca-856e-769d5bc549d3 | -3.70537 | -44.89251 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab31cb01-6dee-3ee2-966e-26fb6f753d46 | -2.36354 | -54.74983 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f055425-7364-30c0-a6b8-3adb694bd803 | -2.60245 | -48.19333 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e676865-27cc-3d3a-9919-ab78d50c9d6d | -2.23151 | -53.7728 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 03833d7a-71ae-3b22-af5a-dfb33a9ad289 | -3.32585 | -49.91221 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0aeb9245-0bfd-3b15-8b5f-0658b48f3e37 | -4.40868 | -48.60831 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 40023f0c-9d8f-3bbc-8b63-51c8fc0c0bf4 | -2.23008 | -46.54943 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c528a2d3-446b-3118-9445-0a6439ee1986 | -3.10107 | -53.32539 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a36590b0-2789-3d3c-99c8-59ee621f0695 | -3.1534 | -54.47651 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9b354bf-1d35-3753-a67b-8d0fa6d2c898 | -2.73623 | -51.71458 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0788d828-979c-394c-b9a8-0dd185dcfdbe | -2.24794 | -53.6688 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| be8035b5-c841-3dd3-9c8e-1f6a078f82e1 | -3.16818 | -48.37197 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee167f2-e8e2-33ac-85c1-0d8c716a582b | -4.19843 | -48.54695 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c45b82d5-a27f-3eac-9886-d2253cd75921 | -1.68381 | -48.47155 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd1b5f1f-a87b-35cb-9994-96e8b80736bb | -1.54739 | -52.59453 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cadb13d3-d21b-3dae-9b21-405270512686 | -2.17869 | -50.97379 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2734631c-1604-3126-9f97-b25c8d1fd749 | -3.11549 | -48.64025 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b230db0a-a63d-3973-9ea6-61c1df337dde | -2.88563 | -51.74165 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c9d7a8a-673a-301a-976c-4b554d5d7c60 | -2.97638 | -47.92075 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c0f2459-0ff5-3ed9-8621-379bd98c881e | -2.84309 | -46.73743 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8cebbf3-9dec-3a00-83ba-ea5af729c85c | -1.67979 | -48.72554 | 2024-11-09 04:55:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b1aa887-4f98-3b5f-ba0d-2c1c2dac38ea | -4.00386 | -49.02274 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e4319ae-9ded-35ef-8e93-f4a6db4ef535 | -5.66219 | -49.99443 | 2024-11-09 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2f64cd0-4b62-3a85-8644-407862f40c07 | -4.13179 | -43.59323 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94101ae1-1e5f-3aae-952a-1f526f6cd924 | -4.48436 | -48.49175 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef7cb713-b82a-3f1d-b46c-4096afac735e | -2.20447 | -51.94508 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08020faa-556d-3740-854d-dddac4ae5796 | -3.72931 | -50.16861 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2810a38-6be1-39f0-8971-449c3b402bf9 | -2.36964 | -46.85965 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7a740198-b030-3f8d-9c58-ed3949b70fda | -3.0909 | -51.11619 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d6ec09f-0e0d-33c8-822e-3e1619d7fa19 | -3.03459 | -53.27267 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 223b91c2-a634-322e-8b5a-2073ee8739a3 | -3.13906 | -53.68435 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37721c94-b0f0-3977-81da-34e24a193182 | -2.42655 | -46.30786 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 73ea6a5c-9882-3854-a826-77607ea493f9 | -1.75332 | -52.68368 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4187c5d-974c-3423-bc37-4114b413f86d | -1.46122 | -52.56372 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e3a75d82-b5bb-334e-b8f8-f9f835181c87 | -1.99747 | -46.39404 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a56c8364-c50f-3c97-b669-b3bd73ad58f8 | -2.96462 | -49.28424 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d5c2bdb-94c8-3b1b-b679-a03265687466 | -5.20169 | -44.92253 | 2024-11-09 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa6a84b-a5d7-3d3e-9ee4-8931d841b970 | -2.37971 | -53.84574 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 550a3324-72b5-39a0-bf79-6a42a80a02ef | -3.80016 | -52.40833 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cafd52a5-96fa-3546-9679-786d43b8e846 | -3.78016 | -47.76207 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6502a9de-f37e-33d7-8b2a-6880f565cd4c | -3.77271 | -53.41963 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82c34c60-05ff-365d-9c77-ba18ddca69e5 | -3.49611 | -51.58672 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63ddd504-d608-3ac3-b4e6-bb9b898bcea6 | -3.337 | -50.07872 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c7c86fcb-2440-374d-bd51-e7540351f5ad | -1.18847 | -51.99061 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f4d94cc-19fa-3c6d-a5f5-900aa02d923c | -3.40681 | -47.58484 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c98c87a-764c-3647-98b0-1a29a3a71b9f | -1.78164 | -52.35105 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b24b311-80ce-3da1-8832-c4585f9dbefa | -3.13373 | -54.25334 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7391836e-07cb-355b-813b-d1f71d6eee18 | -6.27105 | -44.54044 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be143d6b-0593-3e3f-8ddc-a9e9f1e44229 | -0.82215 | -51.76126 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abf9260a-4fd9-37d8-aa0b-f6bc88668a07 | -2.89791 | -46.80022 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4b9d527-5d52-3fb1-bd99-8e74e1a319b8 | -3.23639 | -50.27097 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 12e60dea-a303-3929-a82d-6f6db5c0db91 | -3.75187 | -52.09419 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b5f46b0-03dc-3b18-a2b6-efbad621658c | -2.65004 | -48.63183 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72a15e55-8946-3930-9a32-6da8708347e6 | -4.50254 | -46.39229 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb68e002-940a-3c6b-8ece-8d1120ab3315 | -3.74981 | -52.40059 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb0ab7af-0369-3c75-8113-78abcae853c2 | -3.15863 | -51.1259 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1224da6e-03f5-3bd0-bbb8-7853fcfb3599 | -3.21976 | -53.10691 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefc311e-6c25-36dc-b869-476a6aabb4d2 | -2.23457 | -46.55773 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34f5652d-696d-3956-a255-241566de99d3 | -2.73227 | -51.71769 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbe61800-2659-38cd-b438-eacaffd95779 | -3.8425 | -51.19912 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README92.md)
