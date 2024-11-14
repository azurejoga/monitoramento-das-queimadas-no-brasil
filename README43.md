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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b83baa9-f775-3bd1-a975-027d5cb4764c | -3.79881 | -44.85715 | 2024-11-14 05:01:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d23118b-274b-369f-935b-bb92ceeec450 | -2.40265 | -48.50781 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c03ece4-8b1f-3ed2-8401-c4bea108aa72 | -1.24875 | -51.76147 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3961b0ba-c736-3dcc-ac03-5467ce5765e5 | -2.19775 | -46.35891 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b18b9b6-ad6d-336a-a544-d63061cea56c | -1.39408 | -52.08032 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de71b5af-0384-3ef6-b84b-1408cd34f92e | -2.21194 | -53.71211 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f15acf54-0894-36a6-a64c-8e9f438b9cae | -2.16708 | -50.658 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c242154-e276-3129-bd2e-4f7be4cbb10f | -2.151 | -48.95295 | 2024-11-14 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d0bf1f-8436-3a54-b650-3f3fcfa9e4a1 | -2.07477 | -46.56482 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90490987-c717-3828-b42f-a882301e4aa8 | -1.45039 | -52.24937 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93bfeca2-6441-3cc9-8fbb-97464f13e6b3 | -2.17677 | -48.5501 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf0749b0-5bd2-3bfe-9aa1-ad91ec95a38f | -1.13457 | -53.65687 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cdf0feb-4c44-3883-b2b1-c9ed3fc3b2c1 | -1.36956 | -52.33424 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48e09c66-0df7-3849-a3f8-fd10d9ab9908 | -2.12016 | -50.68395 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ea080a9-1377-3338-aa3e-b5b14d6ce73a | -3.23444 | -50.66516 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03d4c6a5-531d-3ab9-975f-09ac2f37f88f | -1.33562 | -51.41352 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c07bc0a3-e649-3ec1-9250-e9ab82af21cc | -2.15453 | -50.71281 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f6f0bf79-5310-3ba3-8ebb-bd368a73da73 | -0.20422 | -51.49965 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d92a5b-3f29-34e2-baac-965c7561fc36 | -0.91391 | -52.57204 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b77191c-b4c1-3eeb-90a6-4a83bb7c2a93 | -1.41042 | -52.39088 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c59bcd0-bb72-3e57-924a-5397d48f8c74 | -2.15739 | -50.71557 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 422794b7-6816-3c19-944d-5a9817ca9d57 | -3.23755 | -50.67054 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7b1f4b8-fa83-3092-9acb-3e3a6016c46c | -5.56381 | -45.36661 | 2024-11-14 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ea16371-2c8c-3ffe-bf4c-8814d4484840 | -4.15016 | -45.76855 | 2024-11-14 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e241a676-334a-3898-a5c3-0ca1958f8afa | -2.31549 | -50.69046 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3b63496-023b-3448-bf11-2a9ef9a50b36 | -4.9422 | -44.95678 | 2024-11-14 05:01:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 68ec937e-fa88-32df-a238-3e2dff254089 | -1.32757 | -52.45592 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a73676d6-b191-36dc-ae0c-2a6668c82e06 | -4.28274 | -48.20287 | 2024-11-14 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a605d83-a7d3-3667-a4e9-8ff70cd88069 | -1.21343 | -51.785 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62913249-6c0d-326b-85d6-48f651b6606d | 1.07263 | -59.25455 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 606363fc-03a2-3004-90d3-031b7a3322a7 | 0.32493 | -50.9697 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f9295e6-a8ed-3fac-8c83-80cb43170744 | -2.83405 | -56.78658 | 2024-11-14 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4db4d227-1bbf-3688-bc96-0ac3e3534f90 | -1.21302 | -51.7646 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36138fde-8ad8-324c-84b4-de8b89ca33d9 | -1.22887 | -51.77923 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd2e7c65-abbd-32e8-b40f-d26632a78593 | -1.0302 | -48.84673 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89eab38-8b33-37c8-9529-aaa152fee37f | -2.34955 | -51.98594 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa13870-4e7a-3cfb-b3de-0a043e24e0a2 | -1.53935 | -51.11514 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cbe27aa-472a-3bd8-a243-19f342d1bbcc | -2.31787 | -50.70033 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00dc7913-4e2f-347f-b159-41fc94daef9e | -1.05401 | -53.01805 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d647fb99-52d4-32e9-bf72-4bf9935fb2cd | 0.3147 | -50.97554 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eb74c9e-3d77-370e-a49f-bf7934c9d2b9 | -0.03378 | -50.77438 | 2024-11-14 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 625559d6-fd64-3dff-9f61-8fc0a79185a7 | -3.90069 | -50.08814 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c046541a-bfac-33e7-89ff-5aa97da77bcc | -3.44465 | -51.46872 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc38b6f-1b3e-3c81-bc38-bc37a04e75f5 | -2.67434 | -46.81934 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3fcbdc5-cd48-37c0-8d9d-3b34dc7a707b | -0.03999 | -51.74285 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 974f4e98-57d5-3440-8164-48822f05dcee | -2.27494 | -45.34643 | 2024-11-14 05:01:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 61ee27ab-1988-3e21-8e41-25c3b94db66c | -1.35914 | -53.07898 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd6902e-567c-31ec-a8cc-3f3aee91ec63 | -1.36087 | -52.34452 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f29a38b-6c67-3765-a437-ebc2d2e274d1 | -2.15936 | -53.6535 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 45f2157a-464a-3930-b152-57ea7a8d8320 | -5.85844 | -46.41895 | 2024-11-14 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bce6cd07-b783-3c40-ab0e-49427ac3c10b | -0.65329 | -52.36684 | 2024-11-14 05:01:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62cda749-ed16-359c-a1ef-99a07995acce | -4.15563 | -45.76933 | 2024-11-14 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdd15ab7-50e6-3dbb-9edb-c5a1b01a1aaa | -2.34989 | -53.75506 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8780aeb-7c1e-3048-8c04-e36720f76d18 | -4.39594 | -47.27427 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a1576d2-0733-3ab5-9a81-d10318414b94 | -1.80518 | -52.17238 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 493a0dd8-7484-3752-bfc1-3bb3d3d3d8f0 | -2.64082 | -46.17809 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c7176b-e454-3a64-a87d-9d15d996a634 | -2.97255 | -53.27304 | 2024-11-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b99b9505-9e20-3a67-ae96-272b661fd93d | -1.23391 | -51.74745 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b30abea-1d0e-3b82-8a62-20a812c37511 | -2.11687 | -46.5244 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a043bfa-efc9-3713-9cde-93ba51dc444c | -0.83698 | -53.04345 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74bce136-704b-323f-bbc6-2e6787c528f7 | -0.41611 | -51.57575 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b1c5ad0-4dc5-3719-99f1-c69a412c30db | -3.88959 | -50.07932 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 390c570e-3618-3683-9529-af76141d2d07 | -4.14894 | -46.24774 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec1e85f-793d-365e-a41e-d7c1d2ba4bfa | -5.07269 | -45.50722 | 2024-11-14 05:01:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e1e52ce-2512-3899-9df9-f7ba52592f34 | -2.98847 | -45.86726 | 2024-11-14 05:01:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f90b1236-e289-38fa-8047-521a1368718a | -1.2315 | -52.15079 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd720d18-0788-3147-818e-f538bf72255d | -2.87611 | -51.79482 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b2ba83f-8fac-3ecd-9183-7c3b70b8e02f | -0.9869 | -51.78066 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7182bd9d-ed96-3aee-b047-ac83e0c1b386 | -1.56323 | -51.85134 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ac30577-b274-3e59-b2d1-40f0e6098edc | -6.03024 | -48.04158 | 2024-11-14 05:01:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8545ad3-1f2f-3598-8a0d-e1dfe797b27c | -2.2572 | -47.32892 | 2024-11-14 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e692a266-243e-3453-8113-5663d4f954f9 | -4.15511 | -45.77282 | 2024-11-14 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2ec5cd8-fca6-33c7-86dd-702d4abdc02c | -0.98753 | -51.77671 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b793aec4-dab8-343b-849a-22913f26aa68 | -3.74259 | -50.45241 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a620b7f-28fa-39eb-b6d8-fffcae978604 | -3.78219 | -46.05742 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4ec4c74-d721-3d59-8a8f-39414e5e2948 | -6.26959 | -44.54345 | 2024-11-14 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1c4a188-8abe-3107-9669-40466bb6ef3b | -1.13899 | -51.68495 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5a95b89-d85d-3b37-9115-619a389354c1 | -0.17504 | -51.55365 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86da0803-37c7-3c09-b4a7-97df73c482c6 | -2.90264 | -51.79045 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b850449a-47d3-3ba6-975a-4e9bff11f801 | -2.35017 | -51.98196 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b480fb7-2a12-3ae7-876b-16055fdf984d | 1.07092 | -59.24355 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc6f7a51-dffb-318e-9254-83060b1acee5 | -1.4187 | -53.47799 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81d6d0e2-5a3f-3db6-a1f5-ffe7b138afbe | -5.60941 | -46.40212 | 2024-11-14 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b47ca84d-66c0-366d-b795-5505d1e6fc87 | -1.4295 | -52.24615 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff4c3e5b-1bcb-3030-8a6d-bfd6d4608299 | -1.33173 | -48.32949 | 2024-11-14 05:01:00 | NPP-375D | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8928d032-d5c6-301a-b860-f47333c25870 | -4.04664 | -47.22852 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a295374-904e-3a8a-be5f-e8435e140b90 | -1.24214 | -51.78082 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acb948d1-3160-3bcc-8100-992b846e995a | -4.07698 | -49.14118 | 2024-11-14 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c5c1e2-ce38-3fb4-b0e1-b42ae6795225 | 0.04346 | -51.70187 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50138281-f662-3908-a082-c6122a442fba | -4.02675 | -44.67875 | 2024-11-14 05:01:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5fa6670-2b85-3b8b-a5f7-785e5c7a73a8 | -3.56992 | -50.33035 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c60bdb7-dd93-3e9e-bb76-c6faa5d80c3f | -4.438 | -45.9517 | 2024-11-14 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87cc8e6b-28c6-3225-97a7-e38addda6c32 | -5.05586 | -49.64365 | 2024-11-14 05:01:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eda87a6-4af5-3281-99fd-ab943aacb088 | -3.41183 | -50.86174 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42c69ffc-f917-3d57-aed8-17b235e027fd | -1.29012 | -52.4694 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 43703f22-ba1e-30d7-a51f-a5a61b61515e | -1.41925 | -53.47447 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47744b00-8707-3272-ae3f-ce403773d272 | -1.35297 | -53.08922 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f9d8115-5341-3cd8-b135-ad3c9f3caaad | -2.74973 | -51.6211 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91e29992-f33b-3c23-9e1c-ac434a31044c | -2.31715 | -49.19074 | 2024-11-14 05:01:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c455be1f-cd36-34de-a924-c0154f7dad43 | -1.39842 | -51.13033 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README44.md)
