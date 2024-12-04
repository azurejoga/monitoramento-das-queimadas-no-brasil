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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a8b916a-e6e6-3b94-b73a-e1e6fd59cfd0 | -1.73856 | -52.61545 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 99e7755a-7fd3-36f5-9170-13f3b2950089 | -3.48432 | -53.80437 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28dfe250-9c31-3dba-a95d-b82c2ae9d88b | -2.73323 | -51.82614 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecd708a6-3f44-379a-9772-3687ad591262 | -2.79294 | -54.13209 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26de23a6-78d3-3947-a1c1-00e8bed1180d | -2.63615 | -54.09791 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e99a017-da15-3a89-95f4-39ee30357864 | -3.12275 | -54.61028 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4810e321-5f13-391f-94f4-62248f34a1b0 | -2.73375 | -51.82264 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f45ecb2-88b9-3080-b6bc-1caef4d0c80b | -2.20363 | -47.24584 | 2024-12-04 05:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7798c1f3-da83-30f2-a11a-d7d68b7411d7 | -2.9027 | -51.8178 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 088f058f-f6a4-3af9-bea7-89022b62c70c | -1.90256 | -52.85282 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cfa3423-02a3-34a1-8cfe-7ecf17981aef | -3.27861 | -50.33066 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 676da800-e809-352a-9a27-8562cf77f66a | -3.18143 | -54.34205 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13a1cdf2-3967-3887-8e83-b570aae1efb0 | -1.65038 | -52.38226 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d55061f-740a-361a-8e56-56f9f536bae8 | -3.13082 | -54.62277 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 373bbe4a-d32a-36d3-8932-73b9558163af | -1.65578 | -52.37982 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df231117-6a43-3aa0-9a61-04ddf2c4472f | -2.57628 | -54.80254 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b685412-503f-3441-950e-5f905965915c | -3.12976 | -54.62527 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8284e7e3-86c7-38ca-abc5-a59b53ed8dd3 | -2.41876 | -54.02092 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0817540-d753-3611-8393-df94125cdaa7 | -3.28036 | -53.24613 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d2fdb61-cf7b-3113-ba06-f54a1309d5aa | -3.92462 | -52.3933 | 2024-12-04 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acc07a52-2a05-3c34-a4b1-0aa15564a396 | -3.13977 | -54.52971 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1ef37db-9d79-3136-af2a-c70757492ae8 | -2.44467 | -54.03992 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93d42042-1af3-39a4-a4a5-7921589c50f0 | -3.30918 | -53.36054 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3b00270-7148-3093-9d7f-ff42ba93b241 | -2.7887 | -55.35176 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d44cd7ca-c0df-3aa2-b0a2-7a3cee3e709a | -3.22242 | -53.12696 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ca43c697-e5d0-3be7-bd8d-ef6e48e58f30 | -1.31609 | -54.57588 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09c6c1aa-0055-3c7f-b12c-29f6aa8d44da | -3.13148 | -54.61828 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 16f442ed-b711-3e0f-b89c-eda7aacd604f | -3.19571 | -50.64653 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f491a2d-f06a-3bdc-9165-d2d1e63b40c4 | -3.49463 | -51.56244 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22cbc420-5778-3679-825f-e5d96e16d620 | -3.11997 | -54.62836 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d8b9b307-608a-303a-b23a-ec49ee2f2d0f | -3.20167 | -50.64751 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffe333d5-3bb7-323c-b2c6-b00ccf18fd9e | -3.10227 | -53.75654 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bc41e37-da79-3c36-a815-0602719f268e | -1.75859 | -52.62161 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d29e00-f71b-32fe-8583-0b9d528f1316 | -2.99204 | -54.10516 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eeef467-0cb7-3b11-baa7-98aaaeb2a99e | -2.81447 | -53.06144 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bed1718-af32-3e4b-b5ef-232ea9b0675d | -1.9481 | -53.34442 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b45f0e5a-53ca-3333-b60d-3d0331421814 | -3.57525 | -50.30911 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7ddac8e9-17ce-3065-b334-b109079241bd | -1.94704 | -54.2354 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b1c222-12e3-34c2-b71c-6ea92736a1f2 | -3.57551 | -50.30754 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 52a20e98-e5e3-3335-81f1-e168de9bedd6 | -3.05437 | -54.50568 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59f34bcd-aaa1-33e5-9903-e33fea36c68d | -1.68815 | -52.51739 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c47171e1-7731-37b5-85d4-82a5b247e2a7 | -2.90341 | -51.81343 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ae5e5fb-28e5-3598-9334-2c26baf8ebee | -3.25398 | -53.6572 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35b2e893-4c8a-3cef-8e26-ad02f0aece2f | -1.15583 | -54.21184 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b5be354-699b-3695-9ad0-39d64296b27b | -3.81706 | -51.6643 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b671884a-bb84-3560-b034-76d0ff4e6f1c | -3.27949 | -53.252 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34948103-2a7b-3eaf-9fa5-4a31b19e46d5 | -3.72976 | -51.08599 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2076a9b-c683-3f18-88bb-4339b04f4abe | -3.53253 | -50.38583 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90a09038-5849-3546-9289-f5bf627cae3c | -3.3386 | -51.21133 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6b4638d-6179-3abc-832c-3e687d9c418e | -3.11042 | -54.05976 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e79eedc0-b247-37b6-aa41-6126d94cdfba | -1.15634 | -54.2103 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88cc558a-a821-3be8-9dc3-8f13afdbbd47 | -2.63699 | -53.35342 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2987932d-c173-3c7e-9b14-4dd89543fa9b | -2.88133 | -54.12711 | 2024-12-04 05:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c030dd2-ab4b-3d35-89b8-fdac18b80ffa | -1.53547 | -52.68076 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 626312f4-392b-3dbe-90e2-5296a906b43e | -2.56359 | -53.39759 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a9cc1f4-dee4-39b8-8b22-aef75bb75839 | -2.9603 | -53.72269 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c361e2a-1c58-3ca7-a841-23330baf2242 | -2.63254 | -48.06122 | 2024-12-04 05:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35f7a641-e97d-3e65-8501-3bb1a1c0dce9 | -1.49142 | -54.43285 | 2024-12-04 05:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86a5e3ed-10d1-3902-aae0-8760ad60a8e3 | -2.81625 | -53.04979 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b9d09a5-a37c-3f16-9b2a-f9b63e140b65 | -1.75767 | -52.62762 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d37e5190-96fc-32b6-bfd6-01d2c436dbd0 | -1.62445 | -53.53489 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8a51c703-49fc-353c-b876-1970cda8f675 | -2.56743 | -54.0009 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b35d17a-0776-30b6-9610-25e709eb4d39 | -3.25722 | -53.8305 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46ab2e24-2cb4-33fd-9c47-6cea281b3f8a | -1.89705 | -52.84819 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfcfd42d-63ed-3f91-a886-122796aa4274 | -3.10563 | -54.05621 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22adb882-a7f8-3cd1-8de9-9776c4dc3641 | -3.48595 | -53.8034 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 153a13e9-0ec5-3153-9139-68aa2bf1a933 | -1.74323 | -52.61924 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 5e3cb14b-dca4-37ed-afb2-bbc819e112ba | -3.8176 | -51.66058 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95c6eb7f-7bf3-3828-bf09-48707d63e0e0 | -3.06711 | -53.27464 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1c6de3d-237a-396f-9592-287cb42c9d69 | -3.34742 | -49.77098 | 2024-12-04 05:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc14927a-8f61-34dc-87e8-e8a2f9a4d7c0 | -1.65334 | -52.04969 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf8a47c9-ea3d-37bc-bc58-fc4f28ce349f | -1.74413 | -52.61322 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4dbc2cb1-002d-3909-b920-b5e7bf37f83f | -2.69866 | -51.86488 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6ccccd9-bf48-3c75-b195-77702b1faebe | -1.9498 | -53.34572 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d0026ae-2dde-3d89-ac6e-55cabcf48083 | -2.90841 | -51.81777 | 2024-12-04 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10f95d3a-3d89-3514-84b1-11c4b90763de | -3.1793 | -54.33523 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c599f929-932d-38b4-b16a-c62e574ca79c | -3.26538 | -53.64787 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c65b40ab-1602-30a5-982c-4e24aaf54e64 | -1.76371 | -52.6224 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7415186b-0f29-30b0-9f2e-06bfcf51288b | -3.31033 | -53.35575 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 946b7380-30b0-3821-b1b9-80ff60d7c56d | -3.17541 | -54.32958 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9acb2a85-e189-3984-bca4-575af5cd2470 | -3.19951 | -50.64783 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 421fbdb2-1386-3170-9e24-2864c0bd72a6 | -2.46439 | -53.62271 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| effc97c9-499d-3759-b7fa-5608dbb2134d | -3.33921 | -51.20732 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3cb98fd-3b42-3567-b72f-34939e91f05f | -3.25973 | -53.61933 | 2024-12-04 05:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a3746b0-a6e1-3f4a-abf7-3276ba196e35 | -3.19884 | -50.65223 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a823389b-2a85-3236-a2bf-13fead5a112d | -3.13184 | -54.61179 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1e942d1-aa54-3744-945f-6db085a702ef | -3.1175 | -54.61412 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 23b29d59-6876-3d36-afc1-6d3983954c1b | -3.58139 | -50.30999 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3de1d44-ef2d-36fb-b981-3fd72817f702 | -2.82591 | -53.05423 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4586e48-5398-3f1d-a949-66a32f7fa72d | -3.20612 | -50.64451 | 2024-12-04 05:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 662cbd02-5621-388a-9586-7527a8cdd3ae | -3.05703 | -54.49332 | 2024-12-04 05:29:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe07cf63-a972-3f3b-b585-792d72423d83 | -1.32731 | -54.96959 | 2024-12-04 05:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17b9dcbb-5f3a-34a5-87d8-378615603e51 | -2.23862 | -53.6977 | 2024-12-04 05:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 788cc7ca-4de7-3d88-9085-b8ed950bbb80 | -3.58603 | -50.53478 | 2024-12-04 05:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1591b584-c8d8-3a2d-b10b-a2fc3b372092 | -1.65511 | -52.38618 | 2024-12-04 05:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2d66790e-7c5f-33b9-9c71-d26ffdf872d7 | -2.19556 | -47.2432 | 2024-12-04 05:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7daa86f1-a57c-3cd7-9cae-0d3a548c7a9a | -1.48831 | -52.52661 | 2024-12-04 05:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32f7075f-5a6e-3f4e-bf16-49759daff53a | -3.55337 | -51.51659 | 2024-12-04 05:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba76efd3-9144-3252-903c-736f6f89d43c | -2.81076 | -53.05193 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bddfb002-e777-3314-8cf5-b99e616c773d | -2.81209 | -53.04319 | 2024-12-04 05:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README55.md)
