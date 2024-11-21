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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 614bb2e2-e2f0-3f9e-a7f1-2f8152b5b8f1 | -4.10638 | -50.74372 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9df7421f-3602-34ac-bed4-2b027d5ef0e2 | -3.79822 | -52.40278 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8b72123-ef0d-3881-a1b8-b76ef9fac356 | -3.54423 | -51.436 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04846a80-311f-3a21-ad2b-989c30998a18 | -4.66432 | -46.53948 | 2024-11-21 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 87c81d22-6418-3ac1-ad0a-61fca84699ec | -4.14377 | -43.88328 | 2024-11-21 04:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb4ae6a7-15e3-3d5d-8f10-342341a9f2a3 | -4.11337 | -51.05405 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4ef6195-5615-365b-a449-b638f8143d20 | -2.93198 | -53.08085 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a617ec8-f9f7-3418-ac5e-52d18d7d6d08 | -2.62091 | -54.27939 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a3e4ef-fb5c-3ba6-9b59-89f13631ded9 | -2.7708 | -54.0601 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e045b932-ee57-34cd-9294-78cc2c18f194 | -3.42176 | -50.25769 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eb56b30-9c78-376c-a0c1-55978e39e610 | -3.39621 | -50.35181 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a60811b-b6ec-3f8f-9891-a0aed7b1a80e | -6.12417 | -42.51191 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| b7a7c84e-cba4-3571-a960-f8ea59c22ce9 | -4.00746 | -47.97291 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 768b7163-fbb9-3ae6-aff5-155cae1a5aee | -3.10188 | -53.10033 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c282d35-5d05-3f0a-b819-5ab1a8e97f7e | -3.28907 | -53.83379 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 35b7d201-ee83-3118-9b4f-16c03c0df439 | -2.56191 | -54.07024 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b031ca09-27fc-34e7-b9b3-b9b1aea38fec | -3.67164 | -54.27287 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df28e6d7-9887-3d42-b63e-b2051dfbebe4 | -4.06931 | -51.03152 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a9444d3-a14d-39cf-8512-d9f6aa03d94a | -3.27521 | -53.01422 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4c02a86-eaf3-3076-b8d0-8b9ca132359f | -2.82284 | -51.79699 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48f2feb8-1f1c-368d-a280-7f7609ba9325 | -3.61901 | -51.08929 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0332b491-8b3a-32d9-b961-bea84942dd8a | -3.18657 | -48.57467 | 2024-11-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4c1ccc4-81e4-39db-86a7-f66e0c8a0bc1 | -3.38565 | -52.41526 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 166dd165-62a9-3080-962c-effe1e6d6114 | -3.57568 | -54.68468 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc7671ea-c1a8-3fa3-b60e-cbac182510a1 | -2.62097 | -53.97632 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40e40d3e-ba67-3917-ad1e-c517a3d7ad1f | -4.11345 | -54.18608 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad700416-355f-362b-980a-d0f7d2ac8794 | -3.6634 | -54.32503 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a675be14-e5e3-34a7-a797-f150ff5b8623 | -3.2869 | -53.84757 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d1a162bf-df3d-3d6c-9fd7-b2acb2cf0fc4 | -3.5866 | -50.52513 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c01f2657-dc18-3001-9668-fedb637d9714 | -2.8392 | -51.82533 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 482b0d18-1aac-3970-8416-aecfa08095ec | -3.67496 | -54.27338 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85694dc8-2eeb-3408-a84c-d9275774ab52 | -2.97825 | -52.91523 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fd52e6a-f02b-30a9-854d-c2c4b3e2606a | -3.73959 | -51.15071 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3308d23d-2a58-3ea5-9449-cd80a9a45ad8 | -3.81421 | -52.34373 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb5c3861-8d81-354a-baed-2e255b09e119 | -3.53892 | -51.60647 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6082e7bc-0d8a-39d0-8276-52e3109e9eec | -2.75677 | -52.11229 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ce9a315-faac-37a4-a5c8-995daa1593fd | -3.27254 | -53.83123 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4aa03627-fd55-355a-b55a-dcd6ec921158 | -3.2583 | -50.39922 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff39aded-d685-30c8-bfaa-c827747fcabf | -2.7796 | -54.04763 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b11cee91-e911-319f-bb6b-ce409dcbc582 | -3.66697 | -50.44357 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7254fe10-8aa3-3335-b0d7-2bc8d80e8fa0 | -3.2919 | -50.53775 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a191fae-d3ba-37c9-a823-1fc00ded7c4c | -2.92933 | -54.08884 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ec3a198-10c4-37e4-aadd-6692b22f86aa | -3.28024 | -53.82537 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 20f51188-6cbd-30d0-a942-4b05fdc7fae5 | -4.08316 | -49.29441 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4322d35c-a407-34ab-af7c-e7b0112afaca | -2.86304 | -54.0358 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4027d41d-36ca-344e-8c54-07ef55c5ee5e | -4.09361 | -51.08327 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df1574f9-193d-3706-948d-931ceb040add | -3.29631 | -50.36715 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cfc85522-eab1-37ea-a16a-442d2fe67013 | -3.53835 | -51.61016 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1ac2dad-ccc5-3745-89be-9dfef17dba6a | -3.76878 | -51.68281 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7aabba4-562c-3e52-b4a8-ae5034f66045 | -3.51592 | -53.79564 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d19d9e9f-6dee-3948-a16a-817dac3e06e5 | -3.39261 | -50.35126 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c25dc96-a239-3851-b41e-49198be6fb8d | -2.62755 | -51.92181 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50117c39-fb03-3db2-8643-3fdf2a34ea5d | -3.09846 | -51.28143 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4661c560-e58e-33bc-84a8-7397a9502373 | -4.69143 | -48.98046 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c309242-11ed-38e4-9bf5-079e80f13b4d | -3.56508 | -54.68663 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8467cdbf-230e-3671-98c2-af98b8e981d6 | -2.36752 | -53.83744 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66d11307-ceda-3437-925d-34ec5e31ceea | -3.37266 | -50.19001 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b62e176-8ba8-3831-809f-684bd3637efb | -3.19143 | -54.32245 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daeab79e-22c4-315f-af2d-af70ced2d200 | -3.2003 | -54.33097 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1db87407-22d7-3faf-ad3a-e2cf15101bd7 | -3.06816 | -53.22887 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5475b6f-0c49-397f-bc56-c72e1d801859 | -3.55087 | -54.58665 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e98c4366-76a8-3641-96ab-20710f41aa1b | -3.53856 | -50.53591 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ceef726d-b4fd-37b2-af9b-1f7424479b3d | -2.92921 | -53.07693 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e26f324-42b9-3513-ad88-f37f4b45f71c | -2.8397 | -53.96833 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 041aafce-97ce-33be-b5c4-3b90b8355e14 | -5.10536 | -43.17067 | 2024-11-21 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b32ed2b-772c-348e-84dc-e56ca5236989 | -3.30118 | -50.35943 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e83637a-e3e2-3878-931a-f5d8ddbfdf6e | -3.81342 | -47.79873 | 2024-11-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53dbb56c-e656-3931-99d2-a3a944b81be4 | -2.76084 | -54.05855 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e65b0dd-006a-3bcf-ac16-22c951a45cce | -5.23597 | -42.64172 | 2024-11-21 04:55:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 436d5de5-19f0-36e8-9da7-d812f77ae69c | -4.95208 | -47.80464 | 2024-11-21 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f367037-4d9d-37b2-9a01-614fbaff5d1f | -3.54963 | -50.27565 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f672d05-4369-3ed9-8962-297496843cbb | -3.42182 | -53.29127 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db976d56-8762-3b4b-bc85-5684090252d5 | -4.07112 | -50.90248 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34206b8a-ede8-391a-8333-2fa84adbd202 | -3.49214 | -50.11555 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c95385cb-3174-318d-9148-131be49c6b9b | -3.49263 | -50.11284 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc5f743-8666-3622-b313-9cde88efb25f | -4.09128 | -53.6148 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 315b6734-29a4-3ffb-bbc3-45b45095b1e0 | -3.803 | -52.22614 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4696b463-dfaa-3d68-93fa-2e6e42c4f344 | -4.91449 | -46.83834 | 2024-11-21 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cd2d711-2e2b-391b-881d-3b6cb8a54401 | -3.61655 | -52.11697 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b406da2e-2e9b-31f3-bd85-1f042607e1ee | -3.37963 | -52.45397 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61b51b22-b38c-3900-ad21-2cd3e7dd01d8 | -3.91285 | -49.03992 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b73ad43-a2dd-31c8-b79a-040c9dd85d9a | -4.07221 | -51.03599 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e46bbfa-a9e9-3952-93b9-7fe981408ebc | -5.19518 | -47.73867 | 2024-11-21 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eb5710f-61bc-3422-beae-d335e9d0a0f4 | -3.37197 | -50.72172 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19b4b708-b1e6-30a0-8c14-b72142cd5512 | -3.29601 | -52.96792 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a2a6c82-1c82-3854-9471-b196391bf3e9 | -3.45603 | -54.19666 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1da1bee-d30c-3487-be9b-427b448efbbb | -3.03386 | -53.72675 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7e2db35-e15d-3177-b671-9f61337aca0a | -2.88164 | -53.9607 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a0c5010-b745-3a0a-928c-4fa4a3a5b064 | -3.96132 | -46.72698 | 2024-11-21 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dca7bfd5-ff90-3713-b991-f4a2015ca5f9 | -2.88147 | -52.4487 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a508a04e-eba0-3197-8784-c0ada86f8aba | -3.90989 | -52.40593 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c710403-79d6-39ce-a2f8-9338d1f02cde | -3.67441 | -54.27686 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0ee3ea4-8e5b-3cb4-9d83-19152f1dd81b | -3.54757 | -51.52811 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a80e89b1-62c8-3452-a3c7-2235c9405f30 | -2.76193 | -54.05161 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 486c1501-7cbb-37a4-8b32-071fd185b575 | -3.76016 | -52.41206 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bbc1d025-8154-3bce-b070-59971d416ee4 | -2.80499 | -54.01608 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f8e272b-d6b8-3f38-9c20-0457454bbb82 | -3.55418 | -50.24625 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3612c32-548d-3c1f-a050-ba3793eb9ee5 | -2.27014 | -55.98416 | 2024-11-21 04:55:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12694a29-eb61-316a-aec7-a70f1e3f84d0 | -3.73899 | -51.15458 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee5de160-aae0-383f-9bb1-97417327ae4c | -4.95267 | -47.80058 | 2024-11-21 04:55:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README70.md)
