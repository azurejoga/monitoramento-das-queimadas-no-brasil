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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dec12df5-c56f-3f4d-9493-20d747763eab | -4.20774 | -45.47988 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 11bfb432-7c92-348f-833a-166b0c750572 | -3.19903 | -54.3257 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c139164b-963f-314d-ab3d-a6d22b5fd0f8 | -3.47071 | -50.84077 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 712b24a5-fb56-3fea-9d3c-e6fb443d1363 | -1.60536 | -52.2533 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36938f99-8229-3538-959e-1170f5667de7 | -1.77289 | -53.59566 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fcc02a6d-0594-31d8-a169-7f3f4cdd3143 | -3.54898 | -51.5286 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2a9cc77-5aff-38a7-bf9c-efbd0df91884 | -2.73814 | -54.38936 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3996d9db-0f72-3235-995f-4e389db66b54 | -2.54498 | -53.98072 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e69cf9e8-dc30-35fb-ba06-5b9db3ad9e42 | -3.53595 | -51.11037 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c473949a-ed0b-3ec3-a713-113c9f6d2acb | -3.2471 | -54.25777 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f4d81e05-4a07-3f43-8490-514163eb9f33 | -2.22413 | -53.7275 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b99e8285-0596-31ff-8609-33dcf8770a4d | -4.52884 | -48.92798 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 953d721a-a1e1-38be-9110-851f4a0cae18 | -1.72222 | -52.70353 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0c857840-ee6e-38a1-ad99-4632a4c5326c | -3.27932 | -53.82943 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e75955a5-89b2-31c8-b43a-bffc418abf91 | -3.83323 | -51.71363 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 04b8f6e3-4dd0-3cfe-8f10-043dc272eb66 | -3.75669 | -46.13763 | 2024-11-22 01:06:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 134339a9-dba2-325e-86b4-32fb9e1854f0 | -1.26053 | -53.35679 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a2f89f06-0558-3d35-8dc0-250e30c86e2d | -4.20649 | -45.47345 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7d429e23-1dee-30e4-9bd3-4a92a296dc32 | -2.91523 | -53.06348 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5a65eaa6-8e14-3fc8-83eb-3526e02f7e6c | -3.95384 | -51.13055 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bbb19a86-c937-3464-9cf0-36de7f2d31aa | -3.07564 | -53.29369 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 40b74e86-bd20-3db3-aaf8-951cd9ae47a3 | -3.83389 | -52.25048 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 374993f7-e89a-390f-b2c5-a5d2fff22801 | -3.1579 | -50.58096 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3ca38817-17e4-38f9-89f6-a9423bd0460f | -0.94942 | -51.71829 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5cb1b888-d6c3-3d2c-ba1d-3d2e4b65c9da | -2.16062 | -53.79944 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f58621b2-9288-3d6b-9e4f-8c2de6af756a | -1.11874 | -53.39176 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 142ab760-6a04-3248-ad79-3ac22988c524 | -3.34063 | -50.50412 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 563e50ae-9892-33b3-8868-97de7a55c7a2 | -3.52358 | -54.68144 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 742771d5-fa74-3605-987e-870e8c1ad63b | -1.3328 | -52.42381 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f25abe42-b258-3e61-8fea-6383afa57402 | -2.784 | -51.72797 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfd0d095-2771-3132-bc9a-a3ae4bd91b8e | -3.32997 | -53.26764 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ef1c366-b5e0-3f74-a0fc-945e10986a93 | -1.80728 | -48.76657 | 2024-11-22 01:06:00 | TERRA_M-M | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d4ec6dac-3e7d-3ec5-968f-de84d5a3d39c | -4.28479 | -48.22367 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 83956e9e-3021-3a17-b955-9d67ba54c504 | -4.13502 | -54.6627 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 61f87c17-a2f9-3aac-8333-b8af51bbf04a | -1.63752 | -52.41927 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2c653c2f-c902-35e7-9960-90920b96f9c4 | -3.2457 | -54.24776 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 53e82ceb-b10e-3862-8abb-0183ed603dc2 | -2.74944 | -54.12651 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 60149065-0d57-32e5-80e9-297a4bf87e99 | -3.95184 | -47.98181 | 2024-11-22 01:06:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 449f89f6-ebc0-32cc-b39c-1142f54cde51 | -3.18826 | -54.31704 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4c74f3ea-4da0-349e-9cfe-a4d23aad8489 | -1.44192 | -53.4017 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5063bbc1-76dd-3fa9-a3d0-8df5a30c44f0 | -4.13361 | -54.65213 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7acde8f-79b7-347a-8a50-12e4d5532d89 | -2.44663 | -46.53915 | 2024-11-22 01:06:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 394dd254-6b54-3eb9-83b4-8b40060d3e07 | -4.64106 | -49.55055 | 2024-11-22 01:06:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 09c54749-d135-3b5b-a985-383f06373783 | -3.25214 | -54.25074 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 61eae30c-64ea-3319-8c53-e076ba6cf490 | -3.53982 | -52.78695 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1e57b51c-d2b3-3326-b999-86cd5209d059 | -3.17751 | -54.30843 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ea4c9e02-60d5-343a-9ce4-54e15ea0aecd | -0.96865 | -51.71889 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c3f5b60b-5df6-3236-90e0-05f331b0202e | -4.63015 | -49.54183 | 2024-11-22 01:06:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bb1988bb-291c-3cd8-8861-f5894f69254d | -3.2749 | -50.43608 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 840933fd-cc19-345b-807a-72b90e52dab8 | -6.27013 | -44.54797 | 2024-11-22 01:06:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f7c6343a-05b2-375d-97b9-5a855063fa7a | -1.38723 | -52.34704 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 48b3e126-877b-345a-901b-14f3f2bdea8a | -1.46468 | -51.11926 | 2024-11-22 01:06:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 55cce2e8-a7a7-3be0-ba55-0dcd5ef62692 | -2.72722 | -46.09688 | 2024-11-22 01:06:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8c7b3fa9-9e74-3c6f-bc1f-c1e209ef9914 | -1.25998 | -51.7598 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| be454e76-db28-366e-9ae2-99f6f2efccd7 | -4.2322 | -48.63819 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 95eb59bf-4dff-3a14-9aa4-9ff50ffb3196 | -1.26303 | -53.37471 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 676789e9-2a77-3fb5-954b-64c7d6027a93 | -2.05469 | -52.04234 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a2c194d-4911-3544-942f-b7ba58c7eac9 | -1.25106 | -51.76105 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 35e952de-bd18-3488-a7f3-3994fcfa56bd | -3.28994 | -53.85123 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| e94af149-bf94-3ffc-9543-4672cde8eef4 | -5.94988 | -48.06387 | 2024-11-22 01:06:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e1bd5856-b9e9-38c6-a37b-45a0162a8d47 | -4.20954 | -45.49334 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| b432b29f-702b-3a83-8318-725027cf81ec | -0.77167 | -51.76487 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 31426f2a-e320-3e3c-bca1-520e64dd7c3e | -3.14628 | -53.13848 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d5d20eab-5b61-3e75-b152-cfe13c236fbf | -1.39448 | -51.99811 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 64601448-2f91-34ae-8c3a-106cce8708cd | -3.48995 | -51.04301 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ed3285b7-a5ba-30ab-9360-098473ef8734 | -3.191 | -54.33708 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a96c1012-a429-34ec-9549-ed3765d554a5 | -4.48544 | -48.11869 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 949338c1-7b30-3ac2-bcc5-2eebc4a84f47 | -3.28198 | -53.84849 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4f708aa4-0aac-33f9-9866-241d44b7809d | -1.58984 | -53.8019 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 56facb70-6078-364b-a0a2-0e15e7c53028 | -0.92511 | -51.74005 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2c8df4b5-08be-3212-aa71-2eb5a389a6e2 | -1.44961 | -53.39146 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| cd76a306-9a84-3425-ac1d-124c157090e6 | -2.01022 | -54.51937 | 2024-11-22 01:06:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2bd62489-a1f1-321d-9e52-ab4a9520d2ff | -2.43445 | -46.54095 | 2024-11-22 01:06:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bbc68c52-c651-338d-8c18-70cb9c3b8227 | -3.31962 | -52.8634 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 52743a00-9151-3d9a-bd06-50c807aee21e | -3.2162 | -54.24176 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0cea700a-c405-3173-9dc7-64d04ebd694a | -2.19572 | -53.65596 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d91e021d-b24a-3a45-9980-bf275ab837c8 | -3.10068 | -53.74434 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 24a8eaa7-6072-3cca-9e3e-c466d42350fb | -2.75465 | -54.09608 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b6008d08-ec88-3dc3-98d1-db0ea73dfe41 | -3.8948 | -46.1114 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5120a596-624f-31a9-a10e-4946736ec55c | -3.43549 | -50.2048 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b599c44-0a20-3d47-9c2e-3e9e89ebe54f | -4.19288 | -53.5868 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4c8f63f9-4134-3b1a-8f86-4b630d1cae3c | -0.81421 | -51.60571 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a92430bb-1e78-36f9-8a3a-0c77cad7a868 | -4.00559 | -49.92633 | 2024-11-22 01:06:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6a3cde47-ffdb-3044-b6b8-28f9e9bb7cb6 | -1.11165 | -51.75647 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b3838408-9292-338f-9882-f6223b5d886f | -0.80488 | -51.79999 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd441de9-8d7a-367b-be9f-11f46279890c | -3.34195 | -50.51357 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| cbe530fc-7064-3c97-bce2-3f6125e1de95 | -2.80564 | -53.00276 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7d23453f-2965-3f13-b9fd-b5e310169fb3 | -3.2872 | -45.4516 | 2024-11-22 01:06:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| b90b94da-339a-3555-b445-76341b8b5401 | -0.77416 | -51.78284 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8b0dcf27-7134-3693-820a-3ec0240aa42a | -1.9591 | -48.38599 | 2024-11-22 01:06:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| af3a8ba6-1670-369f-890e-c5d77c1d2d06 | -5.81632 | -44.75875 | 2024-11-22 01:06:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| ad62476b-aa55-346b-b4ba-f69f2e00cc13 | -2.71805 | -53.17401 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7f2ea10b-3870-3ecf-b53b-26ed78d45b74 | -3.63988 | -54.32638 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e236e411-7c3c-3272-9d55-d89be2773382 | -2.50294 | -54.15354 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c3540649-d45f-3576-bbeb-823a63b25b39 | -1.96588 | -52.99979 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1d39b8c7-6bb9-3786-b45c-2fda9e7c8c60 | -3.94991 | -47.96875 | 2024-11-22 01:06:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| a0a37318-8ad0-32cc-9503-521478137aab | -3.47425 | -50.00937 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05b14735-f9a9-3635-8939-b5848f48c915 | -4.21489 | -48.65844 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 6845e6aa-c277-33d2-bb21-2975a8c0ed75 | -0.81381 | -51.79873 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 69fe446e-261f-3130-8df7-a988976388cc | -3.49511 | -50.22584 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README6.md)
