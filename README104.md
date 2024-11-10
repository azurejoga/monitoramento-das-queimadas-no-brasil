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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a03dab56-c84f-35b0-92a2-0fc9d9ad9f4a | -4.38923 | -47.24019 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38121a42-0e92-3d13-96e1-a922920b8fab | -2.26783 | -50.68352 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 55896d98-43de-3bf2-8027-393857013623 | -3.05842 | -54.00091 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43601e03-3845-35ba-8807-e66277b63f9f | -3.94868 | -48.14619 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 23f8c8e1-c16d-33a7-a65c-62fa9fd42173 | -3.30316 | -54.48784 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb13261c-a37a-3fdb-b435-7b3671ad4af5 | -2.92779 | -48.31646 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07e42f0a-9403-3263-8042-c8be883aebde | -4.11188 | -50.73077 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 967ce377-e738-35a3-9835-5b6e45fab914 | -3.09062 | -51.11245 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86030ded-ae76-3381-aef4-b64dfcbe37fc | -6.29214 | -47.34362 | 2024-11-10 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cc417fe-e7ce-32dc-a991-5de0f5f5a837 | -2.60698 | -49.19046 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0fa16d4-b907-3295-9a03-3d51206340b0 | -2.61163 | -47.95968 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41cb8437-01d7-3655-9109-73bbcc729761 | -4.33388 | -48.60423 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ac37bfc-756d-3bdc-9eae-33e7dda623d2 | -2.73083 | -49.17749 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4e7168-24d4-3519-ac1c-c894f81c757d | -3.69159 | -45.81445 | 2024-11-10 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 823358d7-cfe8-3785-b459-3dcae43fbc0a | -2.94147 | -49.49723 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23920081-4f73-3a47-89c0-0dda0630c2b7 | -4.38243 | -47.23916 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12f50fa1-6cda-3ff6-81f0-342362f7f2ba | -2.44122 | -49.17192 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5d4c80e-1ee2-32ae-ac75-afec7c832ec6 | -4.60986 | -49.58 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3442a54-e7d7-305d-94e9-c49cae99ed2f | -3.56954 | -53.94529 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 516d4b0a-cb07-365c-82ee-3cda4c02729a | -4.70384 | -43.867 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58aabbf6-e24e-326f-bab5-2c418838742f | -3.82454 | -48.98032 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28048278-3a6e-36a5-8213-c54a2012e52b | -5.54605 | -47.50063 | 2024-11-10 04:38:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16126e53-6beb-333b-8cd3-34bff614fea7 | -8.89972 | -44.22915 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6776711a-5b92-3690-80a8-174c6a23ec9d | -3.44982 | -56.93153 | 2024-11-10 04:38:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82d8ad80-25b1-3246-b545-55c21743732c | -2.86898 | -51.4789 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 782ffdc7-8679-361f-8ca6-1810a6796b69 | -1.40389 | -55.45537 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a65bc02-f9f1-3819-bbce-21c57ad5d969 | -5.35921 | -47.91395 | 2024-11-10 04:38:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41403be9-85b7-3751-8b07-d3787f1e9a2a | -3.68963 | -50.20037 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0c48cfe-a9f6-3e5a-8705-ede881fe9e56 | -5.9765 | -45.36656 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ca0ce208-d178-3451-bd75-f31f74054721 | -2.72695 | -49.18045 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb39bf08-6ee2-34b1-9326-9fb072c890cd | -3.95527 | -48.12581 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 87b522da-faff-3559-a797-3c83247896a7 | -3.02182 | -48.0839 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 976feb1f-2ae3-3081-9c9f-d2489cb3078c | -3.5299 | -51.63522 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa1eeeed-11f6-3a04-9f20-65e2651bcc97 | -3.02989 | -53.26035 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 290a9b77-1be4-3283-baae-7ae4bf7dd970 | -2.92084 | -49.4976 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c16dcac-148f-3a98-b0d0-28d4b1bfacbb | -8.39407 | -44.13134 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a86b35b-23c6-37f6-a168-1c20a9de44f9 | -3.90404 | -48.92907 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13fee56a-7b0c-3e2a-9195-cdb5045de19f | -3.95653 | -49.00457 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf7390fd-73e3-33b3-a0b5-d9020102ecef | -3.52538 | -49.97961 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b2a024d-4840-3eac-aa59-fdd55ac3303e | -2.56077 | -49.25097 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78ea135c-ffd1-3724-bdef-835e159d8166 | -2.2527 | -50.41121 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcdc3fc8-b8f6-3b89-9010-cfdac73b1bb7 | -3.16344 | -49.09592 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22869e0-0d9d-37af-8d75-c986c337e5a7 | -2.04724 | -52.08218 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3be80ee-41a6-368e-845e-ed4db894093a | -4.10341 | -48.97437 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 31b6d500-0cf2-3c82-a235-b07477c83fc2 | -3.19063 | -50.44056 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba516bcd-32c7-3f3d-a946-379a0bbc3b02 | -3.13592 | -50.43623 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9da1403e-57dc-3207-aa82-8aa6a0d3011d | -4.10348 | -45.70428 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14afc237-11ad-337b-a2bb-245c97cc0630 | -2.99328 | -49.50886 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b376d733-256e-3d6e-9755-97b6ca59688b | -2.82473 | -49.44319 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d084df88-c339-31d9-a37b-9445d7cb81cb | -3.11517 | -50.14823 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecf01ad5-cac7-3dc8-b395-5e5c3d57c3fe | -2.76891 | -49.3478 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 8cd39753-ff41-3e78-acc1-4fd77c2feaeb | -3.15187 | -54.4841 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f76dca50-5c2b-36fe-a44d-68be527dfa6f | -2.87055 | -46.6629 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f08f5273-467f-3dd4-a99a-1868fdebc528 | -3.30295 | -50.1325 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10ba61b2-d9e7-3201-9a2e-c88d7f6db66f | -4.31457 | -48.61888 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9a4a6a95-d95c-358a-b0e4-ca74f926c931 | -3.19851 | -46.52827 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e5f5cb5-c535-313b-a195-f3b671a1e332 | -2.06423 | -53.29126 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 665d64fc-82fe-3e43-bf46-6df472523dcf | -3.04955 | -54.86032 | 2024-11-10 04:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bc75149-be18-3ac2-94f1-434db2d8d003 | -3.11213 | -50.21106 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9ebea0c2-f573-333b-b518-1bbd3dd60734 | -4.88557 | -48.60527 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 988d4be6-ef96-3864-aef0-bb42127cca82 | -3.95544 | -49.01148 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a061805f-9b90-3b76-a7f4-e1aed66ca5bf | -2.91182 | -49.3598 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 844e5ebe-4705-3a98-8203-2aeacfa5262e | -4.53446 | -43.56692 | 2024-11-10 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0211ac8-c252-3392-9186-62dc2a2b25b5 | -3.98932 | -46.41085 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8190466-4312-3d29-8e4e-1b9f28340862 | -3.58006 | -50.27618 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5457045c-7f3f-3c1e-9c3d-9f3113c30bd2 | -3.03901 | -49.52322 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e54a0377-110b-3a19-a3aa-7738738c4cf4 | -2.40102 | -50.31171 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5a9d02f-ecc9-34cf-b7f4-0c2dd24d7bee | -3.06433 | -48.03017 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d10b212-8a84-324a-8d12-67950dc5b84a | -8.37612 | -44.13659 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bebd1f51-9524-3e2b-9ab0-5fe7139cfc39 | -2.66639 | -49.84595 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08e71f4b-8bee-3bf1-a92e-9cc3ccee75c0 | -2.9591 | -48.03098 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea303d89-a286-32fa-965e-1e85432cdd53 | -3.2376 | -46.54203 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ea99774-2005-314d-b0b2-51d230d3f510 | -3.347 | -50.35917 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6fde440-8152-3fb4-9290-eb6c3bc7a486 | -8.38312 | -44.11774 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24579f09-4d62-372d-8d42-3a017d9590d3 | -3.82516 | -55.67369 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a280af7c-4e6e-3c8d-a03a-aaab57f25edd | -3.25835 | -48.75323 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3373936c-6276-38bc-8139-25e238cffe41 | -2.98661 | -50.2957 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e0e27b4-0d21-3fe0-874f-8ded58b22f3a | -4.1175 | -49.07589 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef220d08-9530-3b7d-9309-3d632297d9a4 | -5.52008 | -45.40236 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5a48a72-2f0d-3859-9147-17bfa09f4267 | -5.40149 | -46.60065 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4990f88b-a7c1-3ecb-b30a-89ea75e7d83c | -2.65168 | -48.63003 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71871032-3d7a-31bb-8f4c-b2b115c3ca64 | -1.5525 | -54.26014 | 2024-11-10 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fdedd3b-9ca9-36c7-9eea-b142facb895c | -3.94743 | -46.37748 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 716317fe-a0f4-3c0a-a9f0-28c8c3f17fda | -3.2211 | -50.20541 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8061b4ee-c939-3340-b67f-52891d968150 | -3.11459 | -50.15185 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fdf05f2-d6e6-3e71-87cb-acf63b4ffafe | -2.04805 | -51.16036 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44a07968-89da-3fe3-ae6b-2e2c71ef8fbf | -3.82371 | -44.84702 | 2024-11-10 04:38:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 376f6cf6-d92f-32b7-b9b6-271cff1dfd6c | -2.22275 | -50.8978 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6de550d9-2625-38ad-9be8-30e512bf0c56 | -5.149 | -48.23943 | 2024-11-10 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26400feb-8b7c-3427-bacf-018568128445 | -2.93367 | -47.86703 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7b1a75d-d784-356d-a0e0-b2c8ea2dfdfb | -3.0866 | -49.58064 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c7df2b5-2c95-3200-8b18-09d17c2e41fe | -2.7278 | -49.83768 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 043b36c6-c657-3fb8-ac46-4d7367079250 | -4.27902 | -50.66922 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34c20bb8-80c0-3329-a8e7-2d51d6214b0f | -3.3948 | -49.73016 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32980aa8-9fb2-31b1-8a5a-386fc65fdbf3 | -3.32854 | -49.10453 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dd5025d-f5e0-3a17-805d-4183f3576f8d | -2.60605 | -48.31968 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e313929e-787e-3c1d-afc0-107a0daa5acc | -8.42383 | -44.13046 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3296cd92-e7f2-36c9-bac1-f48e7c9412c0 | -3.64056 | -50.18151 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 962e40cd-ee26-3639-9998-34addc9aae1f | -5.23532 | -46.6489 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cf8d164-8c45-3ab0-867d-729ae82030f2 | -2.45892 | -50.29774 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README105.md)
