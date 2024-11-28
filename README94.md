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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c2a0fb-ac7a-3023-b872-edc5d49d2866 | -2.90787 | -54.18323 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da0950b0-5706-362c-bc46-b20fca0013ea | 1.44485 | -55.90195 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8004ffb-b552-3d53-9cf0-c1173ef51692 | -0.1472 | -60.86571 | 2024-11-28 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ca61df6-4451-3f3c-89f0-4a3c4a9df6cb | -1.66701 | -52.73721 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a50cd7c6-a634-30f8-ba56-204629057451 | 1.23973 | -55.9322 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34c4a9aa-08aa-32bc-b72d-2abdf23df752 | -3.49525 | -53.80301 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a8f5a7-7cb0-3c08-87ce-8f9eb0a779f2 | -3.40135 | -54.2854 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fdf1814-2eb4-3660-b767-3b61ba6fdc09 | -2.1832 | -53.77513 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69963faa-9083-3104-ba02-3d03e89cd851 | -2.14406 | -54.83438 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb781c53-d8dc-3b98-b386-0aa3532ff108 | -1.30723 | -55.74522 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7fce3b8-dac1-3008-90fe-b8b586073851 | -3.506 | -53.81306 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 932d5058-bb4d-3d7b-8bbd-bfef2b32de93 | -3.25015 | -50.62405 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 81743b4d-47d4-33f1-b8fe-86cc23ff0694 | -3.80754 | -52.36023 | 2024-11-28 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 882f2cb5-0373-3bcc-a382-3e02688f3035 | -3.08759 | -54.13166 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e933c30-045b-3f30-9956-d91122919623 | -2.74122 | -51.65878 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e45c24d-cfc2-3a4a-acf3-c8cd7d56b94b | -1.15641 | -53.56588 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fca85cff-c8c0-3a5a-8ad2-4ad77245088e | -3.65091 | -51.39153 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6c97f62-c75d-3a6a-8038-51c19e23564b | 1.24321 | -55.96251 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e62e7d6-abf5-34d7-84d0-fba1bc9ca190 | -2.84141 | -54.07598 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de1489ee-9d55-32b3-ac2a-07152b6600b3 | -1.70213 | -52.7575 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7b9f749-3a97-382e-8ab4-e72477bb3599 | -2.31447 | -51.96393 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ba5bae8a-1ea3-3f4b-96f9-d612fa38dcbd | -1.31556 | -51.92392 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e004c862-1d16-3e08-8b58-987228cb88d9 | -3.40168 | -54.28566 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c3ea96f-b4ce-39bd-bd42-b158a6657c12 | -2.24659 | -53.62255 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf834540-16ea-3b9f-95cc-09c348b8d716 | -1.32726 | -51.92605 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c71a112b-4d6e-3eb1-8c45-4e0a8f1f7124 | -3.49464 | -53.80718 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff2a53ee-e546-3b2b-ae32-93111affa9f4 | 1.24464 | -55.96359 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0733742-15ac-304b-b7d7-7417de23c949 | -2.60161 | -53.9766 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ccc8b1a-bd3a-3eaa-adef-0c206c222edd | -1.36128 | -54.65844 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bf9b4df-ff23-3a14-bcf0-1c24cbb87b18 | -1.08773 | -54.0387 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25312a61-5fd2-36af-adf6-a71e270a0762 | 1.44426 | -55.90619 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 225db3d7-033f-3ea0-bfb0-c92c781d503b | -1.8971 | -53.03236 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5468905a-8dca-3137-93d4-ee30a9354fbe | -2.24594 | -53.62691 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cde96f6d-9fc5-3c9c-a5ef-ab0acf3765e7 | -3.09378 | -53.25622 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01ee33c5-3ec6-3714-8ded-601f9e7777f4 | -1.5674 | -55.78545 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22194c8c-ce94-3731-b641-c3f59f7bc6b3 | -3.02722 | -54.02205 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 116521b9-27f9-3494-b211-5fc220b98e12 | -3.11125 | -53.26275 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52b64b1f-31b3-3468-afa5-4ee31dcb91b7 | -3.17674 | -54.32261 | 2024-11-28 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97bef849-fdba-38ab-ac62-e53a28315774 | -1.32156 | -51.91962 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 809d51f0-65c3-38c7-ac32-312a743066f4 | -2.75142 | -54.12203 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d31d2523-cac1-3ab8-8f90-191ff0ca189d | -3.23335 | -54.22424 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ee38363-07b4-3f35-8b86-63b11da9d6d5 | -1.72376 | -52.49277 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 289d8aee-ce75-3427-9976-89c2f2408665 | -1.44081 | -52.59877 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0652397d-0549-36de-a3c7-8fa819076983 | -2.25761 | -53.75093 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeb473b7-064c-357e-9a62-a85d065e8245 | -2.90274 | -54.18034 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75ee74c1-1c83-37d2-a09d-230248fba4a9 | -1.70646 | -52.75946 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b9e2bf8-53f9-32e3-9695-5ec1edcb5d84 | -2.18255 | -53.77937 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3100b682-94ea-330f-b4b1-f0bdcb8d3e77 | -1.68491 | -52.43908 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90f9e29b-6104-3aa1-b2f9-a55b942aa0b3 | -1.0394 | -51.7416 | 2024-11-28 05:40:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 738c7149-fe94-32e2-a620-a3c402769548 | -2.96197 | -51.0087 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7e191a6-d211-3d0f-8baa-42deb55da1c9 | -2.89513 | -51.37434 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1180c473-4313-392c-a579-aaadcda49028 | -3.92033 | -53.66924 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1dbb7623-ec8e-3134-9f57-33ba5319e1ec | -1.16817 | -53.67816 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f8fee05-1272-39b5-87f3-00b797168e17 | -0.9719 | -53.68533 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a9619e8-7ce3-33c9-b7dd-cd44617e1006 | -1.16088 | -53.57557 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22bc2bc1-9e93-3ad2-b8df-46a07a6b4a34 | -2.82357 | -54.0355 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c728cfd-ca47-3c1d-9838-9de19f7e1249 | -1.32075 | -51.92501 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f51bf6b0-bd91-3a79-8031-b1c020b2949d | -1.08935 | -53.37395 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeb440fa-3880-3fd3-87ae-c73335566762 | -1.44434 | -52.59565 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dd69e8b-21e1-3192-8480-9358dc1599d1 | -2.58994 | -53.97483 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9a5c450-4167-3499-84ba-791592a9a821 | -1.03858 | -51.739 | 2024-11-28 05:40:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1334718-d225-3ede-9403-b7fcbea13fbc | -3.10004 | -53.807 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6f7b202-9dfd-3791-940d-607c8eda00de | -3.11807 | -53.25904 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d84a968-c991-3f5b-8af6-3bb8b6c3ec6f | 1.24862 | -55.95757 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4837184f-eafb-3d1f-9050-b5901da06c7f | -2.25697 | -53.75516 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b3382d8-1e13-38d4-a5fa-db558fd033af | -1.16031 | -54.07354 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3480e22e-8781-316f-b32e-baac7baebb0c | -1.16332 | -53.67348 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28bd9627-e517-3308-bc21-3c203ef1100d | -1.66334 | -55.2318 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f756a7de-1e3a-3429-bc4b-c77fc9be16c8 | -3.0882 | -54.12764 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43505768-e884-307d-970e-5163383e5033 | -2.23119 | -55.90199 | 2024-11-28 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab31abc2-9b16-3ab3-8050-bfe6b931f226 | -1.84776 | -55.57072 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 151d02ee-cf5b-3b4d-8e19-5981c044838b | -2.94854 | -51.58746 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 881fc456-390e-349e-ba51-68c0997514a8 | -1.84256 | -55.57001 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f5450b0-cd08-3bdf-b400-200d7bcce834 | -1.64209 | -52.46367 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c65e5452-5aaa-3e85-9153-b7baaed45ca5 | -1.35403 | -54.63246 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11975b73-425e-3f92-aa97-7a0cea6d376b | -1.61098 | -52.62243 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c99d49df-3793-3be7-b2c8-d33879bd26d1 | -3.10532 | -54.98009 | 2024-11-28 05:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6528db0c-b71d-3c7a-87ca-5a4fa5c9dd3f | -2.84116 | -54.11754 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fddf51f4-30f4-34c4-8344-a2453a795e49 | 1.4434 | -55.901 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1fb82bd-4312-3747-9c9c-37afc4dfa539 | -1.98838 | -53.29594 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 182a9b1e-1512-3a5a-ba87-0b318218e801 | -1.69674 | -52.6266 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36e6d6fb-5c30-3c88-874d-c50bce02fba0 | -1.32123 | -51.9303 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87873e1c-f69f-3552-b6e9-21510fe18455 | -1.36481 | -55.01405 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2635fb6-6522-3994-81c1-b70883d6cac1 | -3.1041 | -53.82052 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a4d58ade-adcd-39f4-97a8-d53344072183 | -1.64131 | -52.46872 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57b02b1d-a9ab-3727-afc2-d4e72e4d120a | -1.65397 | -52.47066 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3057e5b6-4da7-3bb2-9997-b70ee884f44f | -3.27388 | -50.61317 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c2d7d75-3e71-380a-8879-d0d5d9246931 | -2.77652 | -54.03447 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 575d1982-98d8-3e48-8d05-d0273f3150a8 | -2.91002 | -51.7113 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8600e2f-2014-31c1-969f-98399dbb139c | 1.44597 | -55.91653 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f023fc63-cd09-317c-8863-1f53ff1d1921 | -2.23674 | -55.89975 | 2024-11-28 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aeb566bd-c320-3759-904d-5a4ca6627c13 | -4.21579 | -50.89239 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19c5aa8b-cf59-3bd8-8290-e11abfeb9012 | -1.64374 | -52.46476 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a703b0c-4252-3d57-9a8d-ad3aad3b37e8 | -4.22501 | -50.87954 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00aad8b9-41b8-3c4c-b3cc-a61b537f7bbf | -3.46036 | -54.48659 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8f4d019-504b-3dd5-9549-4fce6cac4e4b | -3.09307 | -53.261 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36661766-ed1a-3b0d-a76b-c5421a0e79eb | -4.09249 | -54.76682 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6492ba6-c5c3-34ce-83e9-0b3ec4b9cd5b | -3.06141 | -51.06473 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c390faac-7033-355f-85b7-35b7db342afc | -1.16222 | -53.67811 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d4aab29-6be1-3a77-9e30-d0ec8a6d54b9 | -2.60222 | -53.97246 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README95.md)
