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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdeaaa73-fbda-3aec-a9e5-e844090cbfec | -2.6229 | -51.2831 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| a5db0c5a-49a4-3021-be92-0f43999c2889 | -3.2163 | -50.391 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 4931fd8c-d92d-3159-83f4-a4fc052d8f61 | -3.7033 | -48.9986 | 2024-11-07 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5e54f9f4-c817-3a43-9aab-296045f2052d | -2.6044 | -51.3043 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4f19616b-7b76-38dc-b3b2-d12f2d2af846 | -5.4518 | -43.592 | 2024-11-07 00:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 23e27352-5928-3d19-b3fe-bd6271306324 | -2.7639 | -53.2265 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 9b12d282-00b8-3488-b043-94740b31e736 | -2.8016 | -52.9617 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| d550a80c-c2f0-3a2a-ac8f-d0f001edb268 | -3.2164 | -50.3701 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b89c72f8-a57e-34bc-9204-318f6270ab15 | -3.4564 | -50.3832 | 2024-11-07 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bba7278a-842b-3739-a697-c914dc7bfdfd | -3.6602 | -50.2501 | 2024-11-07 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| ddf0e1ce-deae-37f8-9719-24827efe4f7f | -3.4565 | -50.3622 | 2024-11-07 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a01f04a4-e4a1-3739-827b-86acac3a36b8 | -9.7493 | -43.5791 | 2024-11-07 00:00:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b198ab43-45d4-3efc-971a-1d04ff292444 | -3.0396 | -53.2805 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| f174bcc3-5795-32b7-a4b3-7c6270a6993e | -1.2014 | -53.8983 | 2024-11-07 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4e245a83-6050-38d0-8be6-365ce5d5e3f2 | -17.7055 | -57.5186 | 2024-11-07 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 86083be2-7055-33c9-9bf3-f2840efdb03d | -17.6858 | -57.521 | 2024-11-07 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 54a2d1d1-ad59-32eb-b736-920fe6fd0cbf | -6.0425 | -46.6105 | 2024-11-07 00:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| dd12dc8b-a638-339d-9ee8-f46bb087a5d5 | -9.3005 | -43.1185 | 2024-11-07 00:00:00 | GOES-16 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| d34b2c28-c742-3ea4-a07f-d537bb152209 | -1.1831 | -53.8985 | 2024-11-07 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 37ecfe21-5e12-3cf8-a912-34451e591f89 | -6.0782 | -44.719 | 2024-11-07 00:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 306a08be-5fc1-37a2-b602-2ca66a569f22 | -2.82 | -52.9613 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 0768f2f0-674f-3d58-957c-e78f1a886540 | -3.7218 | -48.9979 | 2024-11-07 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| a6b3ec3c-4430-37d1-967c-723deee436a5 | -2.6228 | -51.3038 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 13ddc33e-8da7-3054-8531-1f1f68e9df29 | -1.1283 | -53.7179 | 2024-11-07 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a0c3fbae-9137-3f58-8d33-6dd1c2660feb | -3.0397 | -53.2603 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 316921dd-d8eb-3364-88cc-8f192dcde4f6 | -2.0266 | -46.9958 | 2024-11-07 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| c8616ca4-4c45-3787-b467-eff83a957263 | -3.2346 | -50.4533 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 8bf0d156-2b85-3b40-9b92-31a1e5a0b18e | -2.8352 | -48.6648 | 2024-11-07 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 86c779d8-d9be-3b64-92ff-8d1b775157b2 | -2.646 | -49.8819 | 2024-11-07 00:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| cf662e32-bf1b-3c16-948b-e29e9e88eb53 | -2.6645 | -49.8603 | 2024-11-07 00:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 55de482b-0e0d-3bf8-ae24-c86750e5391d | -5.9788 | -45.3621 | 2024-11-07 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 71f44f80-4c1e-36c3-bbd9-bddfe6262bc7 | -2.7753 | -45.1287 | 2024-11-07 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 571ef369-0999-348c-9df0-49def9c5ac21 | -5.6935 | -45.9443 | 2024-11-07 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 986a0c60-82eb-34c4-9549-0c6a28760b68 | -4.684 | -46.3408 | 2024-11-07 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| f3990048-3491-32c5-8363-74ffedcb7905 | -5.0526 | -46.851 | 2024-11-07 00:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6fb4a5c0-979d-30ee-bbc5-294b6a769016 | -2.8537 | -48.6642 | 2024-11-07 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 0a2d5721-af5c-3963-883d-60158e8030c7 | -4.4596 | -46.508 | 2024-11-07 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 123.3 |
| fbdb4ede-ce90-3e2d-8846-56178e6fc384 | -8.0313 | -49.6341 | 2024-11-07 00:00:00 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9e603313-bea4-326c-996d-5b3c4fe45340 | -1.1649 | -53.7377 | 2024-11-07 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5890e676-ad84-3a5a-b5e7-e8b1f7916c26 | -17.293 | -57.5062 | 2024-11-07 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 52104427-cbf0-327f-a7c8-9947842f61ed | -5.7122 | -45.943 | 2024-11-07 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| facd67c0-b925-3a7a-a954-d202e771ba27 | -10.9965 | -48.9973 | 2024-11-07 00:00:00 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 78c9e401-ce85-3f6c-ba71-ae0de6360609 | -2.82 | -52.9409 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.6 |
| 99d82eb3-e4ef-395a-9cc3-a7f2b70a236d | -5.1395 | -47.7008 | 2024-11-07 00:00:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| cfb1e354-a952-3b17-b1dc-32c9aa4e19f6 | -4.0815 | -51.0084 | 2024-11-07 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| cf99e6af-db78-3387-bbef-df4813e27d0e | -5.0342 | -46.83 | 2024-11-07 00:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3641f7b6-aff7-3589-b619-7658562ad24a | -3.253 | -50.4527 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ac7ebfed-6753-3ac1-a22a-779c61b861ea | -2.7752 | -45.1512 | 2024-11-07 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a97ceee4-9f10-3ee0-b9b9-17573adba3d8 | -3.0207 | -53.443 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 44da3d98-cf75-395f-a1c3-b14cd383a496 | -4.6655 | -46.3196 | 2024-11-07 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| aaaeb903-e9f3-37aa-af35-7a0cb60cf887 | -3.0207 | -53.4227 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 783fafda-10ce-3577-befc-2cd27f642f79 | -2.8536 | -48.6856 | 2024-11-07 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 827533b2-89d6-3e8e-9cfb-f9e4069c76b0 | -2.4319 | -53.6584 | 2024-11-07 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 528a2818-5a8f-353c-855c-591c5a0e001c | -2.8016 | -52.9414 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 25dba241-c3fe-38cd-8437-b64e650a1afa | -3.1617 | -50.2038 | 2024-11-07 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9c98bd23-4433-3520-b7b3-39a98ea75c2d | -5.034 | -46.8521 | 2024-11-07 00:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 105.7 |
| c42877c8-ffd5-35b1-8282-bc2e5b6c8773 | -4.6653 | -46.3418 | 2024-11-07 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 5187dcac-fa55-350a-a5f9-52e131ed77fc | -10.9961 | -49.0191 | 2024-11-07 00:00:00 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| dc946544-826f-352c-9499-bdbef6b35b67 | -4.5033 | -42.862 | 2024-11-07 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4f146aad-3ec0-32b3-a987-12bd1ad3705c | -4.5218 | -42.8843 | 2024-11-07 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5a9113e8-d303-35a2-89b8-56f941879dc1 | -1.1466 | -53.7379 | 2024-11-07 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| e3fb8ab7-3341-3226-8718-0779701325cb | -2.6645 | -49.8814 | 2024-11-07 00:00:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| c858596b-abf0-3d0d-ab06-e513b8ccabe5 | -4.4594 | -46.5302 | 2024-11-07 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| d81ad5dd-05eb-3d52-9a2d-a06fc74d5c0b | -5.3738 | -46.2555 | 2024-11-07 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 4043e8b9-d0e8-3bfc-8b19-971fa3990133 | -5.9975 | -45.3607 | 2024-11-07 00:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 0a552f04-3901-331a-b53a-c922584d7b82 | -4.5031 | -42.8854 | 2024-11-07 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 45451e4d-2c2b-3459-8a71-a14b772e813b | -1.165 | -53.7176 | 2024-11-07 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ad274a75-f7c9-3f90-bb03-ea02efb3cdac | -3.6236 | -50.1884 | 2024-11-07 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e6c9424c-06d9-3c1e-9355-fadcf3299ce3 | -2.4048 | -50.3085 | 2024-11-07 00:00:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 41cf4cc0-f56d-37e3-a197-5f08626e1644 | -2.8201 | -52.9206 | 2024-11-07 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| db5f5229-a9e4-3af5-bc75-dc500b045769 | -1.1466 | -53.7177 | 2024-11-07 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| d8429ad5-20b4-3c25-80b7-16752156f7d3 | -4.522 | -42.8608 | 2024-11-07 00:00:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 4a1831aa-519f-3e96-a74a-bba2c4d23f06 | -2.81 | -52.94 | 2024-11-07 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b698913-930a-347b-910d-d089e1d55291 | -3.9671 | -48.1283 | 2024-11-07 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 1aac549e-37e3-3250-a137-0b532131e6ba | -5.034 | -46.8521 | 2024-11-07 00:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 01018f54-bbe2-349f-baa6-12d0986e4d81 | -1.1831 | -53.8985 | 2024-11-07 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 51f8aa8b-b7b1-3868-b7e7-448194d7554b | -2.8016 | -52.9414 | 2024-11-07 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 13650d4f-a30b-38d5-9d5a-2d6ed47dfd59 | -2.6645 | -49.8814 | 2024-11-07 00:10:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| df047dc6-12c1-3779-9272-2adbc0088c26 | -3.0023 | -53.4434 | 2024-11-07 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| a39d2551-b507-3b2b-b033-1aec070645c2 | -3.0396 | -53.2805 | 2024-11-07 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 7482fe6b-7f0a-34e5-847c-754d4f7fc27b | -1.165 | -53.7176 | 2024-11-07 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7ba2cbe5-63c9-3757-bf4c-ff9caa09fd27 | -9.8755 | -36.1348 | 2024-11-07 00:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 26147f0b-706e-3deb-b843-2814587b0524 | -4.5033 | -42.862 | 2024-11-07 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 99382d21-8904-3594-a69e-647d49f092e6 | -4.5218 | -42.8843 | 2024-11-07 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9e067e47-5d74-3cf4-819b-8c8343f15d14 | -3.6236 | -50.1884 | 2024-11-07 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ef8fa6bd-1eed-3a7d-84e6-435d661cbdf4 | -1.1466 | -53.7177 | 2024-11-07 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| d5ecf90e-5727-3ab9-9d82-4f2fde6b4369 | -4.5031 | -42.8854 | 2024-11-07 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| e73e151e-919b-3bc8-8947-443718af983d | -5.1395 | -47.7008 | 2024-11-07 00:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 0f355eae-1ad6-318e-8e67-0e88d795e03a | -3.1617 | -50.2038 | 2024-11-07 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e9839c02-c55c-3459-8082-c926958d5983 | -5.3738 | -46.2555 | 2024-11-07 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9fd2cdf8-ef00-3462-9740-25e8d8a919cc | -1.1466 | -53.7379 | 2024-11-07 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5428aca5-94c8-3c12-aed4-191a75c57019 | -3.0207 | -53.443 | 2024-11-07 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| c4c9b35e-4b8f-3b49-b9bf-938d693fa79a | -2.8537 | -48.6642 | 2024-11-07 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 776cee6a-7634-3e86-9912-bf1dc02e4d16 | -1.1649 | -53.7377 | 2024-11-07 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 295ca5bb-c12d-3669-a19a-56d6593b5245 | -17.7055 | -57.5186 | 2024-11-07 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| d07b7b15-2f28-3351-83f9-33dfa8241b40 | -4.0999 | -51.0077 | 2024-11-07 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 91c5b145-0389-3f5a-b79c-0b596badbcba | -4.522 | -42.8608 | 2024-11-07 00:10:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 275297fa-72a2-393e-bef9-b7f8e1f2df72 | -3.9669 | -48.1716 | 2024-11-07 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| ce0c8790-705e-38f4-ad50-05ecd5555397 | -5.1394 | -47.7226 | 2024-11-07 00:10:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 5335d6fb-2a78-348f-8469-00c6725b1b8c | -5.7122 | -45.943 | 2024-11-07 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |


[Clique aqui para ver as próximas entradas](README2.md)
