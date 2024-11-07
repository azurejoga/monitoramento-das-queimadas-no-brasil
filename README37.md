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
| 82a7d807-2aa5-3b56-9f70-3c0de72a4089 | -3.2516 | -50.46616 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6e75bc7e-0191-3cd7-9abc-d97275d2e078 | -3.06175 | -52.50085 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b81824b5-3246-3da6-b2bc-b07625c24eea | -2.74193 | -51.89783 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61259fd1-cb11-38a7-a091-85d40921d8c9 | -3.5262 | -50.35755 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e556b7db-2f80-3cad-aa1f-ac78086492d5 | -2.77741 | -52.87447 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2c0b237-96ac-3850-8ebc-34808ac111e3 | -4.06131 | -48.31018 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ed423d6-3916-3328-b571-a5cfd1789c9c | -4.42732 | -47.26065 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d3aa07e0-33aa-35d0-95b1-c9b7079312aa | -2.82687 | -52.90318 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70394c63-17e1-30e8-838e-fefc62a7f1b2 | -2.26496 | -46.46492 | 2024-11-07 04:18:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55222312-be84-3424-bf9f-21b2245ac381 | -1.13982 | -53.72139 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 148a9bf2-be7f-3304-adfa-c9eb458977b9 | -3.04223 | -53.28165 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0108cee-61da-3b83-96a4-9ccabb406147 | -8.0869 | -44.4301 | 2024-11-07 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99de97fa-539e-3d59-b21c-634d7dd219b6 | -2.84906 | -49.81711 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0853f606-85ea-35d1-a13c-9e7da6330075 | -2.8209 | -52.93919 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52e79673-1aea-3a35-8b58-28c2212b9cc0 | -4.5576 | -48.01661 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acd33b3e-a8cc-35b3-9599-9628836f9274 | -6.64265 | -43.40739 | 2024-11-07 04:18:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf291f55-b90c-3693-9250-a32facb5fe3b | -6.04311 | -46.60743 | 2024-11-07 04:18:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21ed50a0-ba18-36be-b87e-de99f60dbadf | -2.46548 | -48.06169 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d686c25-507c-3f20-873d-813c793f3fb0 | -5.34545 | -46.07991 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39165788-bb6c-31d1-a38d-85573a7e3830 | -3.04339 | -53.27485 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce154d08-fa22-3078-8dc6-d53484bae28a | -3.03199 | -53.27657 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba66cc14-38bb-3f18-b8b4-29ae973951ce | -2.65352 | -49.87545 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82c1f48d-e809-3a40-9e8a-053198cf394c | -4.37247 | -47.46423 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a98248d-0b5c-33d4-a7fc-6c59489a8b11 | -2.8077 | -51.80589 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80824293-849c-3414-aa0f-1c584d81bd5f | -6.27555 | -44.73708 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68d6dcc0-dfb5-3fcd-a90f-ae7cde68f93f | -1.51903 | -52.14854 | 2024-11-07 04:18:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d640f94c-baa4-3285-8617-c957e1b22e10 | -2.88187 | -49.37627 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a12d4ac8-4bf5-39e2-92f1-60fa9f276654 | -2.82142 | -52.93601 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf2de75-e17f-3dfd-ac33-dfe8906019e5 | -4.34729 | -48.63161 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf964b2a-d72b-34a9-a8cf-7367879addc7 | -2.42356 | -53.66704 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd2fa11e-d6da-3a4e-9d21-07ad273d171c | -8.35111 | -43.61988 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5155d60e-aa5d-3c94-b7ca-8d9e2cfed5d0 | -7.46452 | -48.33821 | 2024-11-07 04:18:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5810c0c8-f1ea-34bf-a922-6df74ab75d33 | -1.3318 | -54.61469 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bf606aa-8332-3f56-a28f-248476f99e30 | -6.17454 | -44.86258 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5790d742-6e01-3a38-be45-392827137f09 | -3.63816 | -51.79547 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf03536-38f3-3f80-841e-84279b85f52a | -5.15724 | -49.63926 | 2024-11-07 04:18:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e69a1ef6-0336-3069-9516-6d7a9771e297 | -1.14195 | -53.71745 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 31f9a6ed-2dad-3481-83ff-3c8d5743de90 | -6.30023 | -43.84383 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 890db0d1-9f5f-3b31-bc6d-bbdf781015e0 | -7.85186 | -48.21553 | 2024-11-07 04:18:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d28ab0da-dd24-35cd-8219-bc06105733df | -3.12595 | -49.20672 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d8f2f35-d053-3df9-b72a-c5b8b6d8370d | -2.76186 | -53.22785 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 694ae7d6-dcc8-3221-b01b-194a5826b4a5 | -3.78142 | -47.73661 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 643370fc-6f4c-31fd-a006-4458a7ffedf3 | -7.25893 | -42.62761 | 2024-11-07 04:18:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ea70beb-b26d-33a2-a49b-144b47f574b0 | -6.18046 | -46.34167 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d3adfc8-e4f8-33db-b67d-64a72a0e17dc | -6.0858 | -44.71486 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c1bad9-502e-3c7f-ba57-d2f769dbf9ca | -6.23042 | -45.32589 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37a7216f-f91f-3286-b05a-30ee4e4e3cdd | -3.18673 | -50.58248 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78b24af4-e5b9-3561-8946-4e046b3dadc4 | -2.8108 | -52.93444 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 979cdee7-9331-3ca8-bc1c-2d6ed8ba1615 | -2.65108 | -46.74755 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2409cdb3-3d32-37ea-9671-3e867d23f134 | -2.7639 | -53.2265 | 2024-11-07 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| a276c740-2832-3c8a-a6f9-9df4a6152d55 | -2.8201 | -52.9206 | 2024-11-07 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2461fff5-f7f2-36ff-ba63-b99f8b9873b3 | -2.82 | -52.9409 | 2024-11-07 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fcbd9b8d-a2ac-392e-b8d6-6b3ca96f2478 | -2.6228 | -51.3038 | 2024-11-07 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| adbbc814-3bf4-30de-89a9-21e890934093 | -2.8537 | -48.6642 | 2024-11-07 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b07437d1-c347-3ac9-97de-ceee08659e9a | -2.8493 | -49.813 | 2024-11-07 04:20:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f8c6f37a-98fc-3cf5-97e7-24bb38776737 | -2.8536 | -48.6856 | 2024-11-07 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 3d64a4be-bcd3-3a02-9cac-34d8d8c3e087 | -5.9788 | -45.3621 | 2024-11-07 04:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9ae31190-0b96-3ca5-85c3-1d4789269764 | -2.82 | -52.9613 | 2024-11-07 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f6330abc-5a8b-3639-8f75-ea8b8b7a80f3 | -5.9975 | -45.3607 | 2024-11-07 04:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a2f254d4-66c3-3e41-96a3-d6477f383966 | -10.07796 | -50.81772 | 2024-11-07 04:21:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 953bbcf3-5708-37ba-bd3d-f209e31fa3ed | -8.61452 | -47.91949 | 2024-11-07 04:21:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17050b23-55dd-3751-b820-1fc218addb9b | -14.07169 | -44.14347 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44c7067a-8a1a-3a3b-b327-f2e75860b7c8 | -9.74434 | -43.57764 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 829bb367-8191-38be-86ca-d10b31a8966f | -15.2291 | -43.33469 | 2024-11-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4fc28e04-65f1-3614-b14e-735194eaa36e | -8.02331 | -49.63609 | 2024-11-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 790ce3c4-748f-3ab7-a4e7-ea5d58b36f97 | -8.02721 | -49.63674 | 2024-11-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c1d9500-37c7-30cd-b972-3f33b4f0cebd | -16.19503 | -43.70777 | 2024-11-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3127a3ea-a022-3fbd-b0cf-2c4d3f98e83e | -15.86912 | -43.79723 | 2024-11-07 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| beb27971-d932-340b-95b9-9c52129cbdc9 | -14.41146 | -43.18232 | 2024-11-07 04:21:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c25b30b-af89-30db-8be9-e8895594982b | -12.27885 | -51.21546 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d98a6bc-b777-3ded-8adb-3ea5b3d20a2c | -10.14333 | -50.70615 | 2024-11-07 04:21:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b60eac7f-b425-3d98-a45f-86f80485f501 | -16.19714 | -43.70943 | 2024-11-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea5ecd8a-7f0a-3a13-86cb-93d6d57d6243 | -9.72511 | -43.93307 | 2024-11-07 04:21:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7b1872a-01b1-3122-a5d9-5bcd1063d067 | -10.50601 | -44.85591 | 2024-11-07 04:21:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13e26dd3-2840-3007-9631-e961cc58ac38 | -9.74322 | -43.58511 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bb03535-539d-34fb-bddd-3e4963da61cf | -10.00092 | -43.79884 | 2024-11-07 04:21:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4bec904a-0494-3e8c-95d6-6514b6f236e1 | -9.74266 | -43.58884 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8d32a96-5579-37ce-8a72-5cd5cb579c08 | -9.82085 | -41.79589 | 2024-11-07 04:21:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2cd8f6ec-02f6-3792-8f7d-789ae218ba7b | -12.2742 | -51.21833 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7b0751a-0431-37e8-9282-adcdd15a1cd9 | -10.03657 | -44.73187 | 2024-11-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 922ca4a9-75c4-336a-a37b-6cd964a3796c | -13.71826 | -42.89161 | 2024-11-07 04:21:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b2baece1-83a5-3797-b739-ddfb3d6f245c | -9.29862 | -43.12178 | 2024-11-07 04:21:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bba817eb-97f4-38fb-a6ef-8302c77211d1 | -14.06616 | -43.56834 | 2024-11-07 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 838a31c1-9fa2-3697-b442-51e0caee37cc | -9.73925 | -43.58831 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3b1a17c-59b9-3b59-a25c-4da2968aeba7 | -10.03948 | -42.29205 | 2024-11-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d2ad558c-e2c1-3bd1-b4ed-b4aeca6b22d3 | -12.06156 | -51.21622 | 2024-11-07 04:21:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ab20ccb-1935-3020-acaf-09663dc2712a | -10.23633 | -43.98046 | 2024-11-07 04:21:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 276b8c6a-4f20-3122-83d1-a27dbc13fbbf | -11.26935 | -41.04635 | 2024-11-07 04:21:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02dafeeb-fea6-323c-b724-32f61d995079 | -14.19741 | -44.35242 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c5915fa-63c8-3ea9-bc1e-f51fe6d958fb | -9.79832 | -43.86912 | 2024-11-07 04:21:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f08e5eb-e66a-3cab-9806-7b67034bbf17 | -14.79666 | -42.70344 | 2024-11-07 04:21:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfb8fbc5-1beb-39d0-8544-07b8d627dcd8 | -14.07574 | -44.14009 | 2024-11-07 04:21:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 278eeda0-4a43-3fc5-8917-b11a719805b2 | -11.26654 | -41.04414 | 2024-11-07 04:21:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3610cb3c-8840-3a90-9efc-bba933756d5b | -8.02415 | -49.63111 | 2024-11-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c551a3fb-3a5d-3090-8ecb-2f0b6e1d4cc4 | -15.69433 | -43.28895 | 2024-11-07 04:21:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c212461a-74b0-36f2-92c1-1890f6d50d21 | -8.69457 | -47.96159 | 2024-11-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cf3be51-e0ac-3de9-8c3f-41b087c6d68f | -15.23144 | -43.13242 | 2024-11-07 04:21:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e996c172-000d-3f65-a2c2-28eb56648ba4 | -12.27823 | -51.21908 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c17de61-20ce-3893-a042-642019d4346e | -12.21791 | -51.02054 | 2024-11-07 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d16ae72c-a32e-30a2-a52c-a1d29ddc2738 | -15.53088 | -43.99728 | 2024-11-07 04:21:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README38.md)
