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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4952249-76c9-316e-a76d-9c541ac0abc1 | -1.24643 | -51.75295 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08823ac1-48b9-3dee-9a4a-d1b10bc204cf | -1.22052 | -51.78609 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cc96960-f006-38e9-98d3-8b3a011dff91 | -3.74335 | -50.4474 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a9cf58b-1a04-344e-87ee-577d55771c4d | 0.65806 | -51.78054 | 2024-11-14 05:01:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 080e941f-8dc5-371a-8f66-a0b53d525acc | -1.68773 | -48.46485 | 2024-11-14 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0391ccb-16e9-3cae-9c6c-3bb4c266a595 | -3.64148 | -50.59204 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 793686d9-d859-38da-a1c4-391624760cf9 | -1.22824 | -51.7832 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20328af2-1bd0-30a8-a781-73002fabc105 | -2.64803 | -46.17311 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78ae5d5c-8dd2-30a6-b1e4-4dac5e55c699 | 0.69449 | -51.44192 | 2024-11-14 05:01:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d9e49f-a941-3e57-9606-3fea57d027ae | -0.19101 | -51.49911 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42082dd2-a4e0-3f48-9e90-969e23ed50d2 | -0.41549 | -51.57973 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc96d72a-76c1-3dc1-a468-5976dd53803e | -2.67848 | -46.82567 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7ed26a2-631e-35bb-ad43-3da83ae288fc | -0.03678 | -50.77925 | 2024-11-14 05:01:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1468020-fca5-34ae-bb7a-0b9cd3424d3a | -2.29739 | -48.58387 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ba84bc0-09c9-31e0-a92b-dbe44e8b735e | -2.65206 | -46.83266 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87c034fe-4b20-3f4e-9c15-6650b6fa4aa9 | -2.67856 | -56.44996 | 2024-11-14 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 735819b9-3d95-31ec-83cb-ed6e0cfbd34e | 1.30204 | -60.41094 | 2024-11-14 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42f69060-0edf-3dfc-ac77-6a40cc1ec76a | -2.25697 | -47.32722 | 2024-11-14 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8412ee01-385e-3c1a-8dbe-1a4e618a809a | -2.17302 | -48.54522 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d820dea3-bc9b-3ee1-8a19-fbc611d4e9b3 | -3.40248 | -50.30642 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69bba02f-54d9-31d1-aff3-746e1354fcbe | -1.6358 | -53.26837 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0c4dbf8f-8330-302a-9b2f-6760285f831f | -2.63719 | -46.17469 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38bd0ff0-ddb7-3dc8-a50d-40264b9a1354 | -1.38769 | -52.07536 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2de41fa9-739e-36e7-a5d6-fe832f5ad267 | -4.05569 | -47.23539 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ff8cbe7-4e19-3e98-824e-fa8b019644f3 | -2.36319 | -46.98672 | 2024-11-14 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00aef040-0be4-339d-886d-f3542117a594 | -0.6615 | -51.69267 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4558f95-247d-3941-8e37-459849ad5845 | -3.01921 | -51.43962 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99ced304-7ad0-35e7-a300-8a32989d08bf | -1.81839 | -50.96527 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf23772-06d9-33bf-af5a-fd8a207f99a0 | -2.32458 | -51.28421 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 38babc53-46b6-3194-9b38-370fb454c549 | -2.26948 | -45.34559 | 2024-11-14 05:01:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 87f47249-e8ec-334e-84a8-b5a8820f6c23 | -2.20859 | -53.71159 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fb1979d-2293-31e2-9657-e044e3be3eb0 | -1.33237 | -48.32735 | 2024-11-14 05:01:00 | NPP-375D | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91d7becc-eafc-34aa-9631-6842e7561024 | -0.20298 | -51.50763 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a92186a8-06a3-3687-a39b-a6d1f71da3bc | -3.29999 | -43.51429 | 2024-11-14 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e36cedca-e202-3655-a3e9-474bc74a6eb5 | -1.97125 | -53.13234 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d91c791d-e0db-363c-8f3a-cc5a52142e0e | -1.34388 | -51.43173 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b98c24e2-7ad3-3244-86e3-a41eb59ef34f | -1.37021 | -52.25364 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd2deef9-3f95-3ffd-94c6-6548b8d8397d | -2.88396 | -51.79178 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b1e47ab-58e6-3597-99bf-8d9c5bcacce9 | -3.94763 | -48.99215 | 2024-11-14 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e333960-c7b2-33f5-a7b4-41b939bf1d2d | -4.53612 | -48.63912 | 2024-11-14 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c0e4ea6-32ed-397d-b74c-9c67de6ee0e4 | -2.72553 | -53.20202 | 2024-11-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94976916-c5b2-3741-bcc2-1711cc9ba97e | -1.4035 | -52.38981 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07bfe624-4de8-35d8-9292-3a4ecfa1f01c | -3.16261 | -48.36461 | 2024-11-14 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f4d7f12-2bcd-3972-b4f8-e2ef97580cac | -2.8725 | -51.79425 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 924c852b-f3d0-3ad7-8cb9-c6aa41b423c6 | -1.63573 | -46.10605 | 2024-11-14 05:01:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6f05f6f-d297-3d20-832d-56ada431708f | -1.21239 | -51.76857 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5548aef7-547f-31cc-96c4-16a9ea39156d | -2.15931 | -53.63181 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a36d259d-ec6b-32f3-81fe-45e0f43c32fa | -2.2744 | -51.32208 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 643fadf9-bd16-314b-85f0-74c9980a6cb5 | -1.61003 | -52.49798 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec436927-e0e8-3045-ac1b-93e574236e11 | -0.8026 | -51.48432 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baf47328-17a9-3a41-9b00-e1bc6fab5bc2 | -1.63619 | -46.10305 | 2024-11-14 05:01:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3562663e-99e2-3353-9181-c64920fd7c0d | -1.25656 | -51.6278 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d38fca7-1627-3530-98ae-bfd78bf5ce9e | -6.27013 | -44.54502 | 2024-11-14 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0755ec05-0b8d-3735-bd17-468087f0bbe5 | -3.05212 | -45.52278 | 2024-11-14 05:01:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6155188-625b-31b5-ae9d-abcd4ba4e49e | -1.4041 | -51.11805 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa8c30c3-ff71-38e6-922d-c07df6e479b1 | -4.52137 | -46.47692 | 2024-11-14 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98807473-65fb-3f84-812c-83a2419b040b | -2.14879 | -52.09504 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c4d94e9-7b28-3d08-96bb-3b78ccd25c4c | 1.07446 | -59.23922 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e6c9f73-253d-3592-833d-158985234920 | -2.72724 | -51.74126 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71bfccdd-57ed-366c-aea4-12452d2a299a | -3.44603 | -51.47127 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f455075c-6372-319f-9025-83771b0b9031 | -2.32893 | -51.28048 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a1751d35-48f4-38bc-af82-084677a395d0 | -3.77233 | -47.49788 | 2024-11-14 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5989d00a-25a1-3d79-b30a-a0f36614d30c | -1.41279 | -51.11061 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecb247f1-fa8a-39d2-980f-36c1ef60ee0b | -5.03054 | -46.83411 | 2024-11-14 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34b9da0e-c0bd-378e-97cf-7de368e48235 | -3.71093 | -50.6094 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e66b0fd9-ca37-37fa-8f78-148c135bc991 | -1.56262 | -51.85529 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3984dd10-bf5a-358b-bf32-16502fe1dd73 | -2.63985 | -46.18433 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4202bc0c-6ad4-3b87-adc0-381f663054b8 | -2.23873 | -51.42973 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c52f7fb7-d8fd-3f55-aede-8141f82cc56c | -4.16427 | -46.25368 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d542e124-08bb-37e2-a7db-1bce32578e91 | -1.1379 | -53.65741 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d1cab96-32b3-3f18-8c19-913e0aa22ae6 | -1.62494 | -52.51564 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be64b988-d419-34d5-9650-038c1f9937eb | -2.11599 | -46.53014 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caf47ac3-57e7-3a32-8008-1f38b430b698 | -1.72155 | -52.38701 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 207aba5c-81e8-3540-a6b7-07dee44f66d4 | -4.23784 | -46.55123 | 2024-11-14 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdaca7a6-afbf-3244-9c37-36259023bc75 | -2.72213 | -53.20148 | 2024-11-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2bc8c0d-ed71-3d38-8790-9845ab7daaa9 | -2.02758 | -46.94277 | 2024-11-14 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c222ef56-a29a-3148-8eac-8f5cf63f28a9 | -5.05162 | -49.64302 | 2024-11-14 05:01:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 758216be-2391-3593-8ef2-e49e52b42a98 | -0.8694 | -52.59251 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb27c8ba-f5c4-3704-9bc7-8b0a5085a19b | -0.82079 | -51.75594 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5927075-16b2-3d9b-b3af-eb93512e7bc1 | -3.17471 | -50.4577 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c74461f-7ae1-3d52-866d-8ed6fb1049d7 | -1.35111 | -51.43283 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80d893f1-f5a3-30fb-ae32-f00c3483134e | -3.77735 | -46.05334 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9025038d-b05c-37a7-b120-74aeb8085222 | -2.82132 | -46.65715 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8ff484b-1ebd-3c44-a01a-86fc13f1feb6 | -4.39943 | -49.77443 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1e54279-8ffb-3a95-90b3-3efc3442313e | -4.53098 | -48.64278 | 2024-11-14 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1ac89f0-bb96-338f-8b8a-c1431de4b09e | -2.36463 | -48.84892 | 2024-11-14 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 008c7cfb-6982-3778-8192-0cab2effe510 | -4.1542 | -46.24866 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b4849b2-7c39-3cb2-bcf1-e7e7e09b8ae0 | -1.13768 | -51.68761 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 415ccbc1-1ee7-3129-92ef-eb3d776bb0b3 | -2.88895 | -51.68646 | 2024-11-14 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a193759c-b253-3a64-b6ba-8686c7d19fbf | -1.13543 | -51.68441 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cbd9104-c158-3c69-acc2-9922a0ec836c | -2.21139 | -53.71563 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1fd36cf-3501-33a6-8f1c-0adb8e41b2cf | -2.65991 | -51.72238 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 089be462-f291-38d2-86bb-c573571ae3f8 | -1.36453 | -52.33438 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81df9a21-69d1-324c-a9ae-fb3e1f108c78 | -2.05766 | -52.05764 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c37e7e9-6aff-3a7e-ae4f-9fd8e4f7a944 | -0.18035 | -51.49747 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 920ff7b5-64bb-3119-a295-226e25e49ee4 | -1.35802 | -53.08616 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 641fb3e7-8004-3b10-83a6-f5f27fd2e24e | -4.53548 | -48.64351 | 2024-11-14 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3171c198-f323-3ac6-9f69-af3b2766d7c8 | -3.1644 | -50.44926 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb1cf378-f944-31c6-8382-ab9734a674f0 | -1.38707 | -52.07923 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b096334f-dcd8-3a99-a64b-33d8ab9cd53a | -3.94894 | -46.41095 | 2024-11-14 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README46.md)
