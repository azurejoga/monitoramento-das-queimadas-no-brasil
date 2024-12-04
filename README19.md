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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c75557b9-de22-367e-a2b8-ca03bb85bb3d | -13.80786 | -41.57354 | 2024-12-04 03:25:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2f85e2d-e260-3acc-bcb6-040dc4040f53 | -13.80665 | -41.57976 | 2024-12-04 03:25:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da651067-760d-3da3-aab9-4bf8b33a5464 | -8.56103 | -39.59052 | 2024-12-04 03:25:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5ae50c93-9ec4-3f97-a63e-46c82cf0f756 | -7.8642 | -39.50407 | 2024-12-04 03:25:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e3b5f62-fe55-3b4a-9a34-36621b975735 | -11.18781 | -40.32257 | 2024-12-04 03:25:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9c542d80-f293-379b-ab63-d73eab5ba026 | -9.27629 | -35.94875 | 2024-12-04 03:25:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9fd0feb-a911-39ae-a0d8-d49fc1268436 | -8.80302 | -40.47507 | 2024-12-04 03:25:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2a7e21a9-a81b-3060-8e91-e118181a9603 | -10.62184 | -36.77145 | 2024-12-04 03:25:00 | NOAA-21 | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c39451c-32d1-3877-a54e-31d1149f7d2c | -9.40157 | -36.01869 | 2024-12-04 03:25:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 83d7e9e8-1f0c-3603-ad75-0392a66aa428 | -6.2591 | -43.16314 | 2024-12-04 03:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 57e76346-7510-317e-a68c-97b7c0b6416e | -11.18836 | -40.31964 | 2024-12-04 03:25:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce476536-93f0-3a99-9b4c-48046f9fb310 | -8.51113 | -35.73212 | 2024-12-04 03:25:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a0acc16f-e4bf-3492-8cad-9f1e01bf5253 | -10.21866 | -42.18815 | 2024-12-04 03:25:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fbf0e28b-3131-3a08-96cd-e617a51e028a | -7.44496 | -39.75605 | 2024-12-04 03:25:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 72d528d5-c4d0-3caf-92f9-5476e2bcab3a | -18.02304 | -39.51298 | 2024-12-04 03:27:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 609aaf00-a1e2-3043-bca9-28bb75747d78 | -18.73269 | -39.89427 | 2024-12-04 03:27:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 40fe05e9-5cc3-3649-9c96-2ea5366897cf | -19.17475 | -40.13294 | 2024-12-04 03:27:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e827610f-2af5-3b93-b7b3-78151d517276 | -15.77577 | -38.95129 | 2024-12-04 03:27:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6b1a113-7341-378d-8ae1-d9dee5a4b0a1 | -3.259 | -53.6388 | 2024-12-04 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 451040c5-790a-3f36-9a5b-2fc13fba753e | -1.7545 | -52.6159 | 2024-12-04 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 319.7 |
| 7401610a-e66a-38bd-82d8-f73d7fff9eca | -3.1454 | -54.6059 | 2024-12-04 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2ce91840-f7b3-367a-b28d-8a5e1ef9682a | -2.8197 | -53.0425 | 2024-12-04 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8c81d67d-002b-3ec0-a8bc-f341ca3dd2a9 | -3.259 | -53.659 | 2024-12-04 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 69289449-bda2-3864-98e9-d5c9cf209dd1 | -3.1269 | -54.6263 | 2024-12-04 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| beadbd3e-7054-3385-9ab4-65cf0dd042a0 | -2.6242 | -45.7399 | 2024-12-04 03:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 737b86fa-17e1-3a2f-8726-9a6c0a77d148 | -1.7728 | -52.636 | 2024-12-04 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f36af482-7a94-3363-89dd-14c696d67910 | -1.7361 | -52.6162 | 2024-12-04 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 28acc174-6314-34dc-85d4-9137ca90cd65 | -2.8196 | -53.0629 | 2024-12-04 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 6c49157f-cb06-33d6-8b56-3685dff8b865 | -1.7729 | -52.6156 | 2024-12-04 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 36c49562-297b-3244-9b38-89953004be60 | -1.7361 | -52.6366 | 2024-12-04 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 94171ae6-679f-36cf-99c1-ba3e80c1a7f5 | -3.1453 | -54.6259 | 2024-12-04 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| f42facae-ef99-35e5-ba0e-da8b287fb7cc | -2.6428 | -45.7394 | 2024-12-04 03:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b5156eaa-e2b3-3afb-83e3-495a2cd12856 | -2.8012 | -53.0633 | 2024-12-04 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b3bb8f73-24da-3045-b629-db1f21c19e32 | -3.1086 | -54.6268 | 2024-12-04 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| cd6fd12a-3134-3c0d-a4e1-5755b25e4add | -3.127 | -54.6063 | 2024-12-04 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 80b81cb2-91fe-3dec-ba28-16c9e1fd38cf | -3.1086 | -54.6068 | 2024-12-04 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b1518c0f-ff8b-358d-b45b-aa1453dc4aa2 | -5.5693 | -45.1651 | 2024-12-04 03:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 61fe839d-9948-30e3-a917-eecaf46b0140 | -1.7544 | -52.6363 | 2024-12-04 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 261.6 |
| 236ba601-41ce-3fc9-92ba-a7f32013e683 | -1.663 | -52.3927 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e55baf21-1cba-32a9-a2cf-d768f175a61e | -2.8197 | -53.0425 | 2024-12-04 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 63acbc33-1162-32a0-a41a-2ef6ca6f7209 | -3.259 | -53.6388 | 2024-12-04 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fc37b055-420a-365b-8df8-a1a460ff321f | -3.259 | -53.659 | 2024-12-04 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 85eff3c1-bc71-3fad-95b6-de5716520f73 | -1.7545 | -52.6159 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 392f65e1-3666-36d0-877e-ad0cab0b9e71 | -3.1086 | -54.6268 | 2024-12-04 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 811f9584-bb74-31a8-acac-9c25f9a548a8 | -1.7728 | -52.636 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3a93e98d-240b-39c0-ac67-0bdefe819e7a | -1.7544 | -52.6363 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 07eab56c-48ce-3bed-9633-f7ab957da25b | -1.7361 | -52.6162 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| c846a7b5-a3a7-3586-885a-458f456edfed | -1.7361 | -52.6366 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d6633e78-2092-35d7-bfc3-3b9eff6295b3 | -3.127 | -54.6063 | 2024-12-04 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 7836e45e-042a-30e5-aba4-4c48af81008b | -1.6447 | -52.3725 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3631b61a-e48b-38b0-9687-41778f5809b4 | -2.8196 | -53.0629 | 2024-12-04 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| aa110809-9e5d-3252-b33d-fbc182cde48f | -1.6446 | -52.393 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f0ef4c8d-e686-3f43-b9bf-57f8da488e33 | -1.7729 | -52.6156 | 2024-12-04 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1fe287f2-4024-3bfd-8160-66ee8e938e44 | -3.1086 | -54.6068 | 2024-12-04 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c79fc4c0-6dcb-3700-bf77-ad736a6f6a6b | -2.8012 | -53.0633 | 2024-12-04 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 70069ac3-e5e4-3bbb-825b-fe03a0a45e8a | -3.1454 | -54.6059 | 2024-12-04 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0fbb30c9-5dba-32b7-a2b0-6defb6f42f91 | -3.1269 | -54.6263 | 2024-12-04 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 179.4 |
| 91d140e0-7503-3ec4-84b3-4e145b969c89 | -3.1453 | -54.6259 | 2024-12-04 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9307ed69-5113-3782-b7e0-732da8c98ab6 | -6.08054 | -48.07137 | 2024-12-04 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4da13893-e22a-3f79-bdc2-9165c42bd565 | -2.10049 | -46.58 | 2024-12-04 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2cdb7d26-cd0c-38df-9fdd-515f2fc23678 | -5.63174 | -44.83927 | 2024-12-04 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf7c1a63-01df-3f41-82af-78ee1ee22cae | -1.05313 | -46.59042 | 2024-12-04 03:46:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb220ac4-e50c-3057-93d6-55d433f45afc | -6.08192 | -48.07313 | 2024-12-04 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3202868-d35a-3281-a715-30a679531ecd | -2.96459 | -45.20544 | 2024-12-04 03:46:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f58dac-e8c8-366c-9539-3ce4974e29d5 | -8.55934 | -39.59032 | 2024-12-04 03:46:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 57c031dd-4394-3d65-bc24-dddb1efd4d48 | -6.07572 | -48.07217 | 2024-12-04 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 361779f2-c426-3557-b0f0-529bd70df8df | -6.25076 | -43.55735 | 2024-12-04 03:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4207fc4c-d491-37bb-a129-2a9d659f6603 | -8.51253 | -35.73051 | 2024-12-04 03:46:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 95cae983-5905-37af-aad5-e254cfad4927 | -8.11575 | -38.96922 | 2024-12-04 03:46:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 328fa059-c3f5-3aaa-a3b1-e166a99e5202 | -9.41436 | -35.94149 | 2024-12-04 03:46:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f9cb142d-3841-3b56-a2c5-d67dbaa17093 | -9.19592 | -43.15945 | 2024-12-04 03:46:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f5384ba1-fab5-319e-9c1a-78cd4dbe1b50 | -9.27411 | -35.94615 | 2024-12-04 03:46:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79bb46fe-088a-3727-ae87-d91e5369eea1 | -2.10159 | -46.58397 | 2024-12-04 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9209dced-58f7-34f7-8751-6ed56115f0ae | -7.58683 | -37.07502 | 2024-12-04 03:46:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 48aa54de-ba24-376d-a663-42e55814fc7f | -2.09979 | -46.58436 | 2024-12-04 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cbc20b85-df51-300f-a9be-2288295831bb | -9.12145 | -35.64515 | 2024-12-04 03:46:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 363a4fdc-4f72-3657-8299-ccd3442f395a | -9.60303 | -35.89529 | 2024-12-04 03:46:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6a211bdc-15e2-3d9f-a2b1-1d960dcea2aa | -6.26147 | -43.16448 | 2024-12-04 03:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce328800-c179-3fd0-b950-6cb095b4e067 | -9.41097 | -35.94096 | 2024-12-04 03:46:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ce6f1cbb-5910-3b18-abd9-a88088d87ceb | -2.20312 | -47.24649 | 2024-12-04 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc532252-4266-3537-93b1-f80199ead76b | -2.2023 | -47.25135 | 2024-12-04 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f8ec8a9-2aa9-32d8-9a05-ad7de26f369f | -9.32812 | -36.00636 | 2024-12-04 03:46:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f4ffc36e-9d56-3ed7-b39d-0e7ad1a81963 | -2.31882 | -45.42314 | 2024-12-04 03:46:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5272008e-ede4-34d6-bd51-5f73ae263247 | -5.62569 | -44.84423 | 2024-12-04 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93640f75-4624-3987-88ea-2033f34657ec | -6.25533 | -43.55809 | 2024-12-04 03:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4d0fb64-f55f-3cc2-8ae5-e831a3cb39fe | -5.62668 | -44.83849 | 2024-12-04 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8be50af2-e67f-3855-9971-0d510cce4698 | -9.60359 | -35.89162 | 2024-12-04 03:46:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10eef0b8-0d0c-3240-a15a-87e2c515c82c | -8.50915 | -35.72989 | 2024-12-04 03:46:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad9f2937-14df-3a6c-8679-42a495cf6001 | -6.07657 | -48.06736 | 2024-12-04 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a099a66-d2dd-3f72-85b5-aa57a84c0ee6 | -1.5412 | -47.13485 | 2024-12-04 03:46:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b99fe009-58ca-3256-b436-8b725103fe81 | -2.19365 | -47.24358 | 2024-12-04 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf534436-274b-3631-9e0e-2b16d89386b5 | -10.04827 | -36.55963 | 2024-12-04 03:46:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fddba692-1257-33d6-8822-d7d980551581 | -2.06652 | -45.48201 | 2024-12-04 03:46:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3134bc1-a730-30ca-a936-b0d9182a7b3c | -2.19692 | -47.24528 | 2024-12-04 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5d946ed5-9730-3b57-a5bd-f5a1c1b1cc12 | -5.63124 | -44.84212 | 2024-12-04 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12cd3038-3aa4-3379-820c-9eec8b1cc931 | -9.3315 | -36.00689 | 2024-12-04 03:46:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e0157bf-11a8-346c-b07e-c1ddfd727110 | -2.07147 | -45.48664 | 2024-12-04 03:46:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 299863b7-54ac-3f8c-9a22-897640ec481f | -1.54744 | -47.13598 | 2024-12-04 03:46:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab06ac46-1a9f-3598-81f1-02bce8678cf8 | -5.27521 | -46.17332 | 2024-12-04 03:46:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9dd70cc6-98b3-38fb-a39e-8f63519b183a | -6.40445 | -44.05175 | 2024-12-04 03:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
