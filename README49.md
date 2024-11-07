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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0fc537a-4037-3561-9622-e635d2c8fdba | -1.38858 | -52.21242 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3751fcc1-1f09-339a-af65-021771bb1d90 | -2.43632 | -53.66183 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db2c2fd8-d1c6-3146-9913-b35cad107b6d | -3.37253 | -51.05667 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94e1891d-1921-3f65-a64b-56b085d0d319 | -2.81111 | -52.9472 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d92a8b88-0276-3a39-acf1-fc79b3b6e78f | -0.36519 | -51.42168 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d456073-57cf-338f-af27-21a9071d012b | -1.24214 | -52.87014 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8277ce16-3c63-30c4-8b19-e30a1e32dd63 | -1.19401 | -53.70325 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a826556a-302d-3171-8350-534fa96baea5 | -2.94061 | -52.55564 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 144c9765-a450-38e9-b613-76e0d98ea928 | -3.11758 | -51.10821 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ee1b573-b255-319d-99f3-24d58dab38a7 | -3.7423 | -50.07011 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0b561c0-9524-381e-8be7-c1c40000ec5a | -1.14885 | -53.73994 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| beeaa525-2c68-3453-9fbc-41a1b03b6373 | -4.0839 | -50.17041 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3159ff2-3eb7-3f4d-9e0a-3cf37cb9bd5c | -1.36418 | -53.61372 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f705deca-17ba-38cc-97b4-95c165494425 | -2.94773 | -54.20014 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24e5b630-0d60-3242-a042-3b1655837b36 | -3.48438 | -50.38765 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86b66faf-72ab-351c-823a-260ba671c210 | -1.15236 | -53.74042 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c6d9d44-67d4-328d-a79a-a8060d911ebf | -2.75443 | -53.21858 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdd3a8b7-b9f5-3308-8a6a-3cca80355452 | -2.93648 | -51.05034 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5338a0f-5940-348b-8b3b-79b91fe91eaa | -1.94541 | -47.03257 | 2024-11-07 05:10:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 831329be-da0e-383f-95c8-661d0e097cbe | -2.87427 | -51.30822 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45d304c4-31f4-34d6-a443-0d673b73a121 | -3.5831 | -50.23326 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 363ee8d5-5646-3979-a6e4-67317257e669 | -3.15487 | -50.20911 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc94164e-3837-33c1-95e5-6fdddf62d276 | -3.53138 | -50.34592 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cac1a84-1706-375b-92df-67b8fc02b906 | -1.0291 | -47.0616 | 2024-11-07 05:10:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e375ef03-b436-39a3-9c97-d66427914256 | -1.29177 | -54.56408 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5435d257-6feb-39fc-a147-4cb90fd6cbc6 | -3.013 | -53.4399 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74e4fadf-9b72-36d7-8ac1-5a3c7b8b836d | -4.22982 | -50.6448 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3163c2c4-1aa8-32cd-8bcb-32de5b642f04 | -0.895 | -51.76413 | 2024-11-07 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 120881ec-d307-305a-910f-0ab311615aa8 | -2.10392 | -46.47528 | 2024-11-07 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a434cd9f-c3ef-3506-a8d1-edc9f329ecfb | -1.14136 | -53.71889 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2d318501-95d0-3278-9336-636f8d85cc11 | -3.79856 | -52.19068 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b96beab-6d23-3fd7-b3a3-5c47087b3ac7 | -3.02657 | -54.09146 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b7556e-4b85-3c05-8137-259a58791f60 | -1.53619 | -52.00949 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70bf2da9-5e35-3059-9214-7e9118f64c46 | -3.45845 | -50.3793 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 80e2a05e-cece-3a7e-955d-6165bfb28945 | -3.12708 | -51.10831 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecb1d3a2-7e68-3bc0-a613-6b38883e31b8 | -2.55448 | -54.00006 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c38a25b-b5f7-327f-926f-3000bdaed745 | -1.33074 | -54.60436 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5e65a7f-030b-3977-9fde-89acef56123e | -2.82498 | -52.93117 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 356da7f9-0089-3875-85ef-63f5de10c099 | -1.06614 | -53.66404 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f8cb12a-ecda-3c6b-9e0c-59c4800cc102 | -2.83006 | -52.92293 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e762721c-3c30-3f23-96cf-034a17abd10e | -2.03971 | -53.57973 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e3826a1-8513-3b5f-8eb2-889bcd7b44c7 | -2.67972 | -51.83101 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 862ca3a2-b977-324a-b925-ed018c844012 | -0.26333 | -51.66355 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4c58ada-4945-32b7-b707-a01b3ba0f5c5 | -1.26803 | -55.70976 | 2024-11-07 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 251471b9-f515-37ff-8d99-60176b9d43fc | -3.01237 | -53.44405 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de308d93-dcb7-3c2c-a86d-539cdddf7f4f | -2.80821 | -51.80417 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3f7acc2-c7b4-3243-b463-1e0f774f9119 | -2.54626 | -54.00679 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 140b43fa-338e-349a-a180-6ca37dcad4db | -3.31742 | -51.57045 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f2dc90e-8ce6-3b1e-a64f-ae8e44c6bc58 | -2.74573 | -54.12293 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bfbc607-7f73-3f92-b7b9-8eb9f7051f16 | -2.20964 | -53.7234 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 30a8b1a7-5d81-365a-b8e9-d5849f14c6cc | -1.28743 | -54.56317 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4f474cb-4625-374b-8d1e-0c112a99656b | -1.20283 | -53.62396 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 669d64fe-c2b4-39ce-92a7-92d46116ab3b | -3.22776 | -50.44896 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77b75f1a-a15f-358e-a6d6-08b7cf182ae5 | -3.18046 | -50.58195 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34b0c2e6-b3a4-3e50-8525-dc2d25f738eb | -1.41069 | -54.49309 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 863ab6cd-1fc7-3da8-b3e6-d5607bdd8826 | -3.00937 | -53.43938 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f564f18-3c77-394a-a58d-a4be6564af33 | -3.12237 | -51.10493 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032089b4-9d6a-3fa2-96a3-0c5eb04b72ba | -3.09256 | -53.91952 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d7282cc-0c65-3239-aae7-cf80fca717b8 | -2.96013 | -54.16623 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 461c60e6-8b69-3d23-a242-c60de11fbd18 | -3.70776 | -51.38726 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 261c6626-75a8-3ac2-bb9a-a725dbedfedd | -3.11283 | -53.71621 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c939cd84-2291-378b-a624-b30923195d2e | -2.60637 | -51.75907 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1318e335-698d-300d-9d0d-7f6d4059779e | -3.5869 | -50.27015 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a528fed9-b081-37f0-99ee-85df41a5b40e | -3.55131 | -51.48248 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c8fbf4b-78af-3f7b-99ea-bb33a63969df | -3.66687 | -50.25521 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| f74909c5-63f9-3341-9349-136346385bd7 | -3.48058 | -50.38271 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59020e1c-679a-32a6-b164-0c4aa3aa012d | -2.83652 | -52.90575 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 355d1f25-1169-3ac9-8f8d-a2c8aee4fb94 | -1.19459 | -53.69954 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06629214-bfac-3dd5-979e-6de7d377d14b | -3.66239 | -50.25455 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 10e1be74-ff8b-315c-96d2-c2ef80a70869 | -1.29233 | -54.56043 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0547338a-455f-3e40-b5d9-6d76b85c42e6 | -1.08675 | -53.64709 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9168995-e871-3737-9f83-c63e4cb8aec2 | -2.67398 | -51.8229 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b1955fb-4fe8-3f70-a757-046f5b3a98b9 | -3.65258 | -51.24263 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf9e9ef6-347d-3677-9d34-a418d9a09264 | -3.56034 | -51.50632 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 165b3e1a-0bf1-312c-8bb9-80ef902bf783 | -1.44334 | -54.48994 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 183c100d-e705-34ed-8a71-403927fb2e39 | -3.66127 | -50.23148 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c58ce1e8-ed56-3335-804c-25fbd107fd5c | -2.99578 | -51.05552 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0f810b0-f289-39b5-80e0-f8a2628521ce | 1.77779 | -50.43296 | 2024-11-07 05:10:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be72a45d-ecfc-3b59-9d47-964be1975011 | -3.66619 | -50.2597 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 09e2717c-88ff-3f35-8f61-cc68e92a0719 | -3.81704 | -50.63369 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b8c574a-3f23-3787-92a5-7dcc734036d8 | -1.48525 | -52.08485 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4458ac0d-b66c-344c-a70c-4927c55a4710 | -2.77591 | -51.91839 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b512b09-3025-3601-8c90-ad547bbbc56b | -2.67002 | -51.82227 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 997e1a13-4c23-302c-956f-f6c427d0e7f0 | -3.0349 | -53.26994 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79d0c13f-fba1-3fac-8dc9-9405b52c6fdc | 1.78186 | -50.43232 | 2024-11-07 05:10:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 795bbf98-957d-3ce7-a327-a27e01f8fd28 | -1.33131 | -54.60072 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63abdd78-87cd-300c-8f7a-2d74d660c4c2 | -5.04126 | -46.8469 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bafe1010-4c92-3c38-83c5-e373e5920aae | -2.06593 | -48.13972 | 2024-11-07 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edf267c0-6294-3f41-838b-135705772ce5 | -3.18228 | -50.59926 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0defea17-4978-3697-a9e4-5c84f7fa66c2 | -1.07974 | -53.64595 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d097eee-9f8b-349e-b0eb-409833d360e7 | -3.3465 | -50.25872 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16b6d020-8904-31b3-a4c7-708bd5e3ce3b | -1.34264 | -52.1814 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e397036-d44f-3a39-be2a-50a80cef3067 | -3.44961 | -50.37784 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 86d16936-9438-39ae-8f35-3ae256cf8970 | -2.72556 | -51.71401 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49c3a6ed-9ee0-3592-a852-c48e12e2e8fe | -3.70702 | -49.00245 | 2024-11-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8ca52d19-09d1-39c5-a9a4-0955d022c997 | -2.83955 | -52.91084 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 546b8c2f-acc5-356f-8d9f-c03d0d2414fe | -2.80441 | -51.49124 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fe11fa6-3d91-3744-8426-47ac07edab82 | -1.41797 | -55.15839 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2bbe2cc-645f-3037-acfa-4be344c521b6 | -2.78736 | -56.59112 | 2024-11-07 05:10:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48c4db00-825a-325f-aa7d-0159035cb737 | -2.85669 | -51.77995 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
