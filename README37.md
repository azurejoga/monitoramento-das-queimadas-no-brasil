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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 414e088c-7996-3955-a9a3-3643334a9fe1 | -2.73809 | -51.73031 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b6d41d1-31da-3a15-8330-0272f462ab4b | -2.73565 | -51.83184 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4cd7b15-3165-3189-acf2-103ce1c2c315 | -2.73532 | -51.72636 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee0c708c-4720-3c92-8ccf-06fe392f3834 | -2.73478 | -51.72979 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b73432bb-556a-3d28-8237-7d7b6204b2af | -3.41599 | -50.93951 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 332dc2a6-2c2c-3675-8155-562c6d4c2f2d | -2.73235 | -51.83132 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bc1a2a8-4954-3bb7-be9f-5696cf81afe4 | -2.73202 | -51.72585 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8405d8e0-d395-3bea-b895-eb7b8a990d44 | -2.72482 | -51.70715 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fac8544a-f09a-3dfe-92d0-1f4e45e65465 | -2.69925 | -51.97732 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9df0e5b-cdd6-3fc2-8504-30a5185a619b | -2.69871 | -51.98075 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec8f1b89-945d-3f1f-9e33-77a8d6430536 | -2.64955 | -51.75183 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb780162-44a1-305a-8307-86eb1812aedb | -2.64901 | -51.75527 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f5a96ec-6cea-31f0-a27b-cb18f3ffad23 | -2.64888 | -51.71308 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e37a6670-04b3-3711-9cd9-be7903b26ee3 | -2.64847 | -51.75869 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90d0dcd5-c11b-3f4c-a1bb-0d1fed25fcb0 | -2.64625 | -51.75132 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44b1c1a9-49c2-30e7-911a-aa104a06dd99 | -2.64571 | -51.75475 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27722cc0-a7bb-38ab-aefb-9018d06bee34 | -2.64517 | -51.75818 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5ff4f8e-4f8c-3f90-a033-bd1ce7e994f2 | -2.64349 | -51.74738 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4a7821e-02ae-33c4-82b7-1dec029775b2 | -2.64295 | -51.75081 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3905331e-63b2-3882-84dd-b2c5d8bfce85 | -2.64241 | -51.75424 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7feae519-9e7b-3e74-a05b-54f2cf56acdb | -2.64019 | -51.74686 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77298c8e-52f4-3868-9f12-c0203fcd6d22 | -2.63965 | -51.7503 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a3dd6f8-3884-31e9-8f40-6eebc30abab4 | -2.63904 | -51.73264 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c82c6fd1-4cf5-372d-a1e8-0b23b6716059 | -2.6385 | -51.73606 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd5df2bf-061f-3c05-a277-82af9baf1ed6 | -2.63628 | -51.72869 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7323fa78-b689-311c-822f-37a5d3efb1c1 | -2.58574 | -51.92112 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cab7c40-f30e-3625-afc2-190d1ddb61ea | -2.58244 | -51.9206 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b1b9a9-d314-3b7f-8cbf-0bcd35bd996f | -2.5819 | -51.92403 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44b47227-fc3f-3fb2-a21d-ff6b66ba3748 | -3.54064 | -51.03078 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc9aefdd-9d8b-39bf-89ae-4f3a63de4752 | -3.53761 | -50.85779 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b65c162c-7649-36e4-871c-ba8f0e8130ae | -3.39498 | -51.42097 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f673b60-bb82-339b-9b13-f330224c34c9 | -3.39238 | -50.80628 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0d7175d-d130-3d0b-82a4-5ace47bc7c19 | -3.39167 | -51.42046 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7643de44-81c1-38d7-b621-0dcbd18fbdc1 | -3.34358 | -50.75244 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0120384f-e9b5-3c7a-92e3-d4a43fb38284 | -3.30328 | -51.26821 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 729ae4c7-b60d-38a6-b2ee-7fdec38baa69 | -3.29996 | -51.26769 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5a91223e-8a22-3630-8b44-76976552c3ce | -3.18801 | -51.33241 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1b6b8cd-7cb4-3101-9845-7c46eea82f53 | -3.18747 | -51.33587 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 115d42fb-bf78-3582-9a0e-752dd21392e8 | -3.1872 | -51.25078 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 347007f0-49bf-36c9-beec-6d1a6c300c8f | -3.1847 | -51.3319 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d4b2300-a474-3b3e-a215-073749674c0d | -3.18416 | -51.33536 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f126f5aa-1e09-3315-85a1-e725c264892d | -3.18212 | -51.21804 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a910dff5-4440-3958-bb69-5852a707aea6 | -3.18135 | -51.15754 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0ae02d2-b699-397b-baa7-7d95484c1349 | -3.1788 | -51.21753 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63ee87ef-cf77-3326-b8f6-ee4a07d1d2bb | -3.15864 | -51.12882 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a4d104f-396c-3c0f-a685-ef4883a5a40a | -3.15586 | -51.12483 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36549b36-2163-3d7d-8e97-6ca1a193bf41 | -3.15532 | -51.12831 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac71d7a7-57fb-3da3-9626-c9c00b186d44 | -3.15477 | -51.13178 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07812efb-683e-3a5a-a5ac-7b8d427894d2 | -3.14291 | -51.03371 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da08ac65-df85-3071-92ca-742f6db7be06 | -3.14013 | -51.0297 | 2024-10-31 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 233a4295-3d78-3458-b84b-6a5d54b621d6 | -3.07447 | -51.25427 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec46a8a0-50ec-3059-b58c-b557e1b9ac5d | -3.03764 | -51.44654 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9db7589b-c820-3671-a11a-36154fa04d9d | -3.03433 | -51.44602 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c013281-973c-3a4a-87d3-84791e360be3 | -3.0261 | -51.45533 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0cf3b30-1031-3a21-8491-99b521888151 | -3.0231 | -51.45125 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad028475-59b9-3658-863a-a664d3b8ab2c | -3.02256 | -51.4547 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff0a35a6-63bf-313e-b6e5-bdc4e2b2e833 | -3.01979 | -51.45074 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14210e2a-bb83-379b-a750-3623e192327a | -2.99079 | -50.9852 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37604e03-b3c8-37b8-a498-ed6757a47d43 | -2.8989 | -51.48448 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5ac95995-92d9-3ad5-8d51-23e32fb9b4fb | -2.89559 | -51.48396 | 2024-10-31 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6671f5d5-49e5-3bb3-a89f-1578bbc56de9 | -2.87909 | -51.30847 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e14bd120-bf9f-3f14-bfb3-e76881b0003c | -2.87855 | -51.31192 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cb6ff5a-d089-3ec0-a086-4784d5511ef4 | -2.87578 | -51.30796 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04a321b-4c12-3835-8aec-da92ebf5c4b7 | -2.87524 | -51.31141 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb059164-45a4-34aa-9ea2-ef0aae305e76 | -2.87193 | -51.3109 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a385c45-b874-354c-b0fb-a83434ef25b5 | -2.82227 | -51.3455 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91d20bd4-9cd5-3283-b3c6-ffb50f1c552b | -2.81896 | -51.34499 | 2024-10-31 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f21a738f-9c1c-351d-b2d1-4925cf75c39e | -3.85795 | -52.08537 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10ed66ee-0dfd-33fd-a5dd-e169fb7fa718 | -3.84846 | -52.03815 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c8766b3-5b67-3751-9247-7ea748f80492 | -3.81989 | -52.04778 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa451a2a-0a57-32d9-a458-0fc4b189f51f | -3.67477 | -51.84579 | 2024-10-31 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc133b4f-6762-351a-a4b6-56288861e71b | 3.56762 | -51.26718 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd680028-80ea-3265-ac9f-f05c79dfeba0 | 3.54105 | -51.2713 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 528a56e0-3d75-3dd6-8e0d-41049a087698 | 3.53827 | -51.2753 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcceaadc-738b-38af-b0da-1d18a8e70ea2 | 3.53773 | -51.27181 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cc4191d-6994-3ca1-bbfb-4a4944f6afd9 | 3.53495 | -51.27581 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dc9ceac-e5c9-3976-b21f-9986f9fd47d0 | 3.47167 | -51.50058 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 295a8ec6-48e1-3452-ae32-8437c493f362 | 3.45943 | -51.50968 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61c62759-1777-38c3-9428-cc118e7d0edc | 3.45888 | -51.50616 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c961b4c-a144-3b0f-ab15-d70b6b6ed3c1 | 3.44503 | -51.24342 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85d5a06f-f4cf-3d77-9d98-2710d1249869 | 3.44117 | -51.24045 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56a4ef77-55f8-31d7-b776-00b6a8bdc8c8 | 3.43839 | -51.24444 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 497e1016-b40f-3c54-b02c-0c0f4d15e6fa | 3.43562 | -51.24843 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d67dace6-687f-3cc7-b173-6d7a9badf099 | 3.43507 | -51.24496 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9970a54c-bc6c-3e10-9ab4-23ba4181c35f | 3.43284 | -51.25243 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fa8edbe-1714-3da2-b27b-a841385e46f0 | 3.4323 | -51.24895 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f610e3f-0432-3860-a439-45c6ae8d912f | 3.35467 | -51.36121 | 2024-10-31 04:49:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5bed8bb-11c5-3c63-a30a-b0ad1cc75f5f | -3.25279 | -53.33893 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5b407f2-c7ae-31f4-b9ec-5bf13c2d8e93 | -3.24943 | -53.3384 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2f1cc88-8558-3c43-8a02-76e1f890d3d2 | -3.2494 | -53.36047 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f5da14a-6d5a-3779-8fb2-6ef8898559a8 | -3.24884 | -53.36406 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 126ca3b0-8683-3357-80d6-0abaa455d8e7 | -3.24606 | -53.33787 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b6fd761-429c-38ad-9788-94a45bba813e | -3.2355 | -53.27393 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03094696-70d2-33d4-b6f5-624af18918a2 | -3.23494 | -53.27748 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 913701e5-6111-38b6-a769-114824a05e58 | -3.23214 | -53.27341 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 790c58b3-b54a-3ba6-b146-2de97a7898f9 | -3.23158 | -53.27695 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ccad69-663d-3b67-8c87-6cf6187a8229 | -3.20162 | -53.40071 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d80b426e-e4eb-31d0-986d-53fdf8baecf1 | -3.11953 | -53.12498 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4cca625-4112-337e-9af9-c958e9447773 | -3.11619 | -53.12445 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc90a48-e9a3-3403-813c-a29bc0f39d33 | -3.10614 | -53.12289 | 2024-10-31 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README38.md)
