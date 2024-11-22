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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23a9ac43-a212-399a-bdac-e249f2815e29 | -0.04481 | -51.23469 | 2024-11-22 05:29:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f3378616-fc6a-315b-abd8-4a72988e9fbe | -3.57026 | -54.68539 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 340f72d3-c2ad-318e-a8e4-68edab3f2f95 | -3.337 | -53.33887 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ace8e58e-52c9-3450-a67b-bb2d6e5928fb | -4.0208 | -53.77914 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f8fa8af-f354-37e9-91a5-5b928833fc6f | -3.41344 | -54.66427 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7f6708e-9446-3242-befe-d3a3e4517974 | 1.37056 | -55.95648 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2c96228-a725-3da7-a2ff-0725515412ea | -2.80822 | -54.01805 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0736e467-25f7-37ab-81e3-2815fa6f39b6 | -3.24532 | -54.24346 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 40af4301-1d9e-3817-b800-d12d9d5196ca | -3.28555 | -53.83171 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72f09f98-0c4c-3fa0-83bd-fa12fe923cc9 | -2.58483 | -54.03916 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e9c93e4a-f581-32df-a619-4c2054b6b77b | -3.28807 | -53.84876 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33ca1fa9-aa1a-32ee-a6d0-1470243c58c0 | -3.64416 | -54.32405 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 194c05c2-b7ae-3460-8c84-7109bb01a4b6 | -3.28885 | -53.84336 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3cd868c-1c12-3560-83bb-91b005eab169 | -3.27061 | -50.62306 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d23ab3bc-039b-321f-8071-1d514a3e3bd2 | -3.50849 | -54.72008 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 163fd65c-b1c2-3532-8467-880fa886cc51 | -4.18722 | -53.578 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f3a987b-b368-3325-a1ff-a0d485e63dcf | -3.50531 | -53.80009 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c44d72db-ac26-3e61-a3fa-4a483ab697b2 | -3.28636 | -53.84085 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3a069a57-9a0f-32bc-9a26-216d6cd3396f | -3.27198 | -51.42472 | 2024-11-22 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7510556d-cd87-3053-92ce-30bd89e15b09 | -2.73745 | -54.13174 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30032ea1-973c-3baf-b77d-b98a88b3f308 | -3.10939 | -54.29185 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6d55c1c9-893f-3711-ace3-eaaa81c6da93 | -3.11681 | -59.92881 | 2024-11-22 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11378a4d-ccb4-3f9f-b8f0-e21f502328ba | -3.19912 | -54.32862 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a344b958-24e9-3cc7-9e1e-a6eaf7d8173f | -3.73671 | -55.55057 | 2024-11-22 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80d1a40e-f865-30cb-b6fa-4d75a61bcfcd | -3.26773 | -53.83209 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 460fe58e-a898-3f35-b1b3-cdbb3e27c27b | -3.28472 | -53.85163 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e6f3bb4-7727-3f82-9460-ac974a5f16ed | 0.46955 | -51.34123 | 2024-11-22 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7834e57f-28a7-3a59-afbc-cc84fc619815 | -3.11005 | -53.99822 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac13cc16-ed31-3f82-aa49-43d0dc418ebe | -3.19307 | -54.32508 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9e5f5444-df07-3116-8774-39a3869a0d67 | -3.47394 | -54.54464 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a710e25d-c87e-34cd-9451-a86ecafba56c | -2.74219 | -54.13247 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bb35380-4527-3dbf-96fb-18621585fcb8 | -4.09075 | -54.04569 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae686ec8-22de-3199-8345-7273132cdd26 | -3.2865 | -53.85959 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c09ace84-9b82-3974-90dc-f10095146de9 | -3.25404 | -54.25007 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d1c2e2c9-97a2-349a-8784-3d63c12ae3f4 | -3.51471 | -50.80838 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3845ba2-7ba2-3ba9-bf34-801c1705c677 | -3.28069 | -53.83079 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ffbb9ab5-7353-3cbd-9e02-668b713a69f6 | -3.66873 | -54.65309 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d03afd0-bdb3-3208-b384-0bb2adbe07c0 | -3.28149 | -53.84007 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a96e173-81cb-3c4e-b451-7e6b55e31d85 | -3.56667 | -54.22366 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| ce533e79-876e-3ae1-84c1-f1982b73d193 | -3.22569 | -54.23795 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b22f695-b7f5-3a24-be98-57f00df8ddfe | -3.21471 | -54.24635 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0b6ed8c8-45a7-33b4-b8da-41394bae6f89 | -3.2964 | -54.7269 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 858d05bd-d957-3dc7-a968-3f6e85962fa0 | -3.28964 | -53.83796 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1f70b03-4716-345c-9ea0-f43200e5327f | -3.42106 | -53.28738 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f02005a-e059-3b78-aecc-1f6742d80985 | -3.33832 | -53.33005 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3978b5b8-086b-37c1-a71f-cc1471e8b608 | -4.11655 | -51.05604 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35ec2b6d-b59c-3b3a-b0cb-25d0fe95cdbd | -4.19854 | -53.4983 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1c1a1f2-cfdb-3d96-b127-43437577a9b0 | -2.81226 | -54.02396 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 99e55369-3ccd-3b1b-bc0e-f24ba75602e2 | -3.46638 | -54.56329 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2990f27-ada8-3f8c-928b-c7b47689b37f | -2.30755 | -53.60105 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 97309d93-f8fc-3a39-be8b-64d86fdd776a | -3.10601 | -53.99228 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cef66bd-14ff-376f-b23d-deec33703ae8 | -3.27663 | -53.82435 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 8697d587-8033-3212-9e12-5ec64658ec4c | -3.73032 | -50.43799 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bef7d106-8806-36f6-a1f3-1250d3890064 | -3.19514 | -54.32281 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb7a8f2e-1f2c-3b60-80f0-d65683a47de6 | -3.29042 | -53.83254 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fef12fa-e318-3620-810a-70e2a728753b | -4.1136 | -51.05669 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c4cbe31-6dda-36c6-8b06-0284848ede82 | -3.23731 | -54.2319 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ad665fe9-41fe-3e14-951f-a0462486291c | -2.56537 | -54.00288 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2e4ecb4-4cde-3bd1-9288-ce5e65ce9f4c | -4.11955 | -51.05761 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e596a692-3de1-3c0f-bb06-41cf2b2f0de6 | -2.44815 | -53.68098 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 212f7937-ffa0-399b-98ba-b2a7e9d8acdf | -3.83155 | -52.25856 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a2bec367-9683-3815-9147-d4fdf4e66ac6 | -3.24679 | -54.23344 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 150b4008-8874-3c5a-820d-6998d8643ff3 | -2.50475 | -54.24557 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b1bd108-fdae-386a-acdf-35d2a175c5ea | -3.25004 | -54.2443 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6e9abd34-cc5f-3a56-8208-356204c559c4 | -3.85807 | -52.35306 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 901b57c0-656a-3876-b8b3-51fc98827257 | 2.37143 | -50.77861 | 2024-11-22 05:29:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 474b5225-c51e-3a30-ba63-0c3a89986720 | -3.84207 | -51.14137 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba555c3e-40b0-3068-ba64-2540ee6b82c6 | -3.0065 | -50.96798 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c2959e1-f45e-30fd-921e-928ba3509c84 | -3.51366 | -53.81175 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ca47e73a-2a5d-3cd6-8b8a-94d1fd6984ab | -3.27663 | -53.83926 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c16a267-d5f0-3f2b-9ba2-c9b0fe4328e7 | -2.62433 | -51.79856 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcce39e7-367c-37e3-8f0a-5c3c610a05a3 | -3.34161 | -53.33513 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40e2a68e-842b-337a-aad6-1227b076b79e | 1.3674 | -55.96209 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 323cf336-ef55-3176-9257-60919d83df79 | -2.78758 | -51.40999 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 48d8de65-82bf-332e-8fde-6f53caf0a423 | -4.12847 | -53.97327 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71dde315-656a-3228-9945-a99374b10def | 0.87099 | -54.63768 | 2024-11-22 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9d88cf2-2d8a-3a11-b5e7-c15cee3566c7 | -3.28801 | -53.83005 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87c6d984-0858-3d5b-93ee-d2210a0a0902 | -3.55509 | -50.52032 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 78633a68-35f7-384b-9477-4f58487531fd | -3.24386 | -54.25341 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e6e6c23b-1402-3c7b-a0f9-695f09691faa | -3.51183 | -50.81124 | 2024-11-22 05:29:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45e2f27b-e895-38ad-a1e1-7961e1ea0842 | -2.45831 | -53.70023 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 696fb6c3-e46d-3567-8391-fceee9756c78 | -3.57448 | -54.68252 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| de1d00c0-c3ed-3808-946a-69173a19f40e | -2.50878 | -54.15391 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 84ba1ace-15b1-3379-8e05-fd705deb37fe | -3.64025 | -54.32441 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 586cc768-375a-3b87-8c35-464106c03b93 | -3.55692 | -54.58466 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4de00738-31af-3ab2-bc5b-8dfb852027bd | 1.38235 | -55.95459 | 2024-11-22 05:29:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f95cb98-4819-3e1b-8b75-41a46aee308b | -3.83194 | -52.26232 | 2024-11-22 05:29:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2a2fb701-4746-3838-8d5d-87d9aedc4428 | -3.23657 | -54.23698 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b354a8b1-ba82-381a-9a18-aaa0b0fc41c1 | -3.24858 | -54.25423 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 961d9e48-5a4e-34de-b9a4-149f0b046e74 | -2.22345 | -53.73129 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48256aad-e909-3083-9bec-cdfae3b78cb4 | -3.20051 | -54.25186 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e8309cf0-89c7-3c38-ba40-e8433c644436 | -2.82666 | -54.02502 | 2024-11-22 05:29:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0364e879-cefc-3a44-bc86-91d306e0fbdd | -3.21945 | -54.24703 | 2024-11-22 05:29:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| adefef40-cb60-3d33-ad1d-cf451f9cb9be | -3.01255 | -51.00862 | 2024-11-22 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e4224fb-d925-35ed-965b-8843ae3b30f5 | -3.28228 | -53.81981 | 2024-11-22 05:29:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bbe6335-3194-3614-a551-265aaf356614 | -3.10712 | -54.28724 | 2024-11-22 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cb64db46-b29d-33c4-af2e-863a3a737a08 | -3.0393 | -54.84878 | 2024-11-22 05:29:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ca4e46b-8d86-3e25-ab56-35ad42eeb713 | -3.57947 | -54.49744 | 2024-11-22 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d79867f5-5649-3841-bbde-7cf10b7abf72 | -2.95216 | -53.71386 | 2024-11-22 05:29:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e065244-cfc8-3a8e-94d0-f6fb315faa72 | -3.85651 | -52.36387 | 2024-11-22 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README57.md)
