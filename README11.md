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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 594f1380-ce8c-37a6-93ec-25c5b0dc8f9c | -3.5446 | -47.3855 | 2024-11-08 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 055e4f2a-1dbd-3709-af9a-c8c0ec1343d3 | -2.6228 | -51.3038 | 2024-11-08 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 71074c84-8b0c-3a25-b16b-3178e20cb729 | -4.5395 | -45.6794 | 2024-11-08 02:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| fa892bc7-6790-328c-9de8-1f75bdc549a1 | -4.521 | -45.658 | 2024-11-08 02:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2ac2fdaa-fdd7-3486-9e75-e4ecf766ce44 | -2.7832 | -52.9418 | 2024-11-08 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f5ec3f5b-caec-3c75-bcb4-b99acf368541 | -4.6832 | -46.4518 | 2024-11-08 02:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b24216e5-6ae8-396a-ba50-723315f10fbc | -4.5022 | -45.6815 | 2024-11-08 02:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 1a9665f7-dc73-3b3a-8c7e-6a3ba645525d | -4.5209 | -45.6804 | 2024-11-08 02:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 274.8 |
| 2a9d445f-c218-3da5-b5a7-3a31bfd71072 | -2.82 | -52.9613 | 2024-11-08 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c98eed36-c0fa-3f82-b60e-243f5acae56a | -3.9669 | -48.1716 | 2024-11-08 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| fb3f4db4-9ba4-3efe-9ab7-192e7c76e828 | -2.82 | -52.9409 | 2024-11-08 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| c4fb7b4a-2e7d-3e5f-a461-2ead336a6fe5 | -2.8017 | -52.921 | 2024-11-08 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b6e59bcd-1348-344b-bb78-c2a918552494 | -3.5447 | -47.3636 | 2024-11-08 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7b6b2acc-6ddd-3115-bc19-f55a27e1316d | -4.5021 | -45.7039 | 2024-11-08 02:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3548666d-39a4-3cce-9c97-bb771d5fdec8 | -2.8016 | -52.9414 | 2024-11-08 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 181.3 |
| a71d43b1-a7ea-37a8-a790-2400cffc1b8f | -2.82 | -52.9613 | 2024-11-08 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9cb286dc-6a1f-3e5c-9592-9905fe24fb2e | -3.1642 | -54.4654 | 2024-11-08 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 9923eb01-98bb-3e6d-b0c3-418ac71a826e | -3.5447 | -47.3636 | 2024-11-08 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e41f8353-7bde-3ba9-b5eb-6271783bc800 | -4.5022 | -45.6815 | 2024-11-08 02:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 7510c908-98a4-33a7-80f5-f9e27a0aaa18 | -3.5631 | -47.3847 | 2024-11-08 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 9fe081bc-6304-300e-b4ad-537439bf0f92 | -3.1458 | -54.4859 | 2024-11-08 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 726ff882-c742-364b-bbb5-2719874402bb | -3.1458 | -54.4659 | 2024-11-08 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d85f048d-e6a2-3516-9942-88992dbec6cb | -4.6832 | -46.4518 | 2024-11-08 02:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| bad94b57-da7b-3429-87ba-b5ef3355f4c1 | -3.967 | -48.15 | 2024-11-08 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d80d08c7-8334-30eb-8342-cb2df558571e | -4.5209 | -45.6804 | 2024-11-08 02:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 314.7 |
| 86e26b5d-7055-3f87-98de-a33eea5213a0 | -3.5446 | -47.3855 | 2024-11-08 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 01e04b99-9b16-3e50-ba42-7cf71fb643e3 | -3.5632 | -47.3629 | 2024-11-08 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 00375400-4453-3a46-bcc7-c2124da1d712 | -2.82 | -52.9409 | 2024-11-08 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ebd59ec4-468b-369e-867d-a148a745f6ad | -3.1641 | -54.4854 | 2024-11-08 02:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 2302d037-6512-3995-95a9-f34df9b3cb1a | -2.8016 | -52.9414 | 2024-11-08 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 1f5ab14a-9ce0-36a9-893d-db6c0ac36ff6 | -2.8016 | -52.9617 | 2024-11-08 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| e150c739-e5f4-3253-92cf-2535c2c9baf9 | -3.9669 | -48.1716 | 2024-11-08 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| fb0eaffa-c042-3c1a-ba66-8b13833b48fd | -4.521 | -45.658 | 2024-11-08 02:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 301d3a75-747e-3ccf-bf18-488986537739 | -2.7832 | -52.9418 | 2024-11-08 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4fca4bcb-72fe-3276-9b4c-9a09983052fc | -3.9854 | -48.1708 | 2024-11-08 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| fc066c30-9d47-34b3-a290-247e562aa63d | -4.5207 | -45.7029 | 2024-11-08 02:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 138.4 |
| fdf9dc13-718d-382c-9f32-19f9a8915e51 | -3.5632 | -47.3629 | 2024-11-08 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 32987d4e-3e22-3634-8027-ae3fa7dfe45e | -2.82 | -52.9409 | 2024-11-08 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ff2f28bd-0687-30a2-9344-6e1ff6cc5dcd | -4.6832 | -46.4518 | 2024-11-08 02:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 62bc5ac8-20de-3624-8546-77a0a25b0395 | -3.1642 | -54.4654 | 2024-11-08 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| aabe97ea-1acd-3413-a46c-9c67ba475a44 | -3.5446 | -47.3855 | 2024-11-08 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 29ef1249-4e2e-39cd-9b73-f4b0cbf4925e | -2.6764 | -51.8189 | 2024-11-08 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4b275813-7bbd-3241-aaab-9e50830b1288 | -4.521 | -45.658 | 2024-11-08 02:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| db2ff5d6-42ba-31f4-a6bb-8072a245f29a | -4.5207 | -45.7029 | 2024-11-08 02:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 141.7 |
| d2e5cbb7-bcc3-3ffe-a6c2-db7580fcb130 | -2.82 | -52.9613 | 2024-11-08 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4a421e5a-773f-3b84-b829-52f20e62a60c | -4.5209 | -45.6804 | 2024-11-08 02:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 316.2 |
| 0e6f8488-b7ae-369e-8fc1-a2e152d9abd2 | -4.5395 | -45.6794 | 2024-11-08 02:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c22dab93-a124-3a02-ab8d-7e18f774b13c | -2.8016 | -52.9617 | 2024-11-08 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 17a88ff5-f5d7-33d6-a806-1935ddcbd60e | -1.1489 | -52.0099 | 2024-11-08 02:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 35e8eea6-b3eb-3b4a-8b7d-014de9bf790d | -3.5631 | -47.3847 | 2024-11-08 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| dfa88147-1037-30b1-918b-671c6a6b4968 | -3.9669 | -48.1716 | 2024-11-08 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 06cbac62-3a36-363b-9c2c-655eac8da3b6 | -2.8016 | -52.9414 | 2024-11-08 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 64019548-bc5e-3b6f-8b16-630a1dd563ef | -4.5022 | -45.6815 | 2024-11-08 02:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| c76d0a78-925b-302c-9643-ea649c31c113 | -3.9854 | -48.1708 | 2024-11-08 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1bd622d2-e169-397a-89b1-92d4580f11ac | -3.967 | -48.15 | 2024-11-08 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a44e372e-acad-3947-b01e-0db923aa18b9 | -1.1489 | -51.9894 | 2024-11-08 02:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bc6d6414-a415-3b14-9833-6b3162766d88 | -3.1641 | -54.4854 | 2024-11-08 02:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 351e1c09-9c63-34c7-8ecf-0f39d1c4409a | -2.7832 | -52.9418 | 2024-11-08 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ccfbca05-4309-3c13-b97e-fde56b36bf52 | -2.8017 | -52.921 | 2024-11-08 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5991d803-2350-3637-81db-c6d41701ad6e | -3.5447 | -47.3636 | 2024-11-08 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 0d790662-e778-3d4b-b0cf-657a7f82d372 | -3.9669 | -48.1716 | 2024-11-08 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 85e05e8d-3837-3d43-aea5-0c00566ab54a | -2.8016 | -52.9617 | 2024-11-08 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 34fa6e72-ed3c-35e1-9aef-4cc35a24f3c1 | -4.6832 | -46.4518 | 2024-11-08 02:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d3bdf4a6-eab1-34b2-b8fc-025cc8c94383 | -2.6764 | -51.8189 | 2024-11-08 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| bb95c57b-3a43-3fbd-a366-b72b373bbec8 | -2.8017 | -52.921 | 2024-11-08 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 628f95ee-2160-3e69-a88a-c6fb274f0eb6 | -4.5395 | -45.6794 | 2024-11-08 02:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 5388a320-b394-33ac-90b8-b194d464d70a | -3.9854 | -48.1708 | 2024-11-08 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7be25321-1066-3ba4-a477-0ab861174f68 | -3.5631 | -47.3847 | 2024-11-08 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f50fa9ba-6380-3e07-8ec6-a46cfbcc0d69 | -4.521 | -45.658 | 2024-11-08 02:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3eb92517-2610-3987-b8f7-c92b1807bb77 | -2.8798 | -46.774 | 2024-11-08 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 39764b4e-26ad-3afb-9912-1c3a66a41427 | -4.5207 | -45.7029 | 2024-11-08 02:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 68d39330-2688-3c3b-afa8-b87be85f4513 | -2.8016 | -52.9414 | 2024-11-08 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 7ac58a3e-7aa6-3f98-ae7a-ded19fc56bd5 | -3.5446 | -47.3855 | 2024-11-08 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7ebc15e5-7390-32ec-80df-89a07c6aefd1 | -3.5632 | -47.3629 | 2024-11-08 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d21b61f8-bdc5-3817-a2fd-c0aaabbe0f03 | -3.1642 | -54.4654 | 2024-11-08 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 041f2b63-95be-333d-bcf9-6c92c363fdff | -1.1489 | -52.0099 | 2024-11-08 02:40:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e7119bfa-7127-3b4a-9afb-666dfc181ad7 | -4.5022 | -45.6815 | 2024-11-08 02:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 125.7 |
| b9d5e99b-54c6-3b64-8bee-8958f595af5e | -2.82 | -52.9409 | 2024-11-08 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| edb05aee-7d27-312c-9f2a-0daae1ac412a | -4.5209 | -45.6804 | 2024-11-08 02:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 287.6 |
| 2dcdb59e-c5b9-3fd0-9788-5c2bb9ac35e3 | -2.82 | -52.9613 | 2024-11-08 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3157126e-4a27-35bd-8e27-7fdf80556f3e | -3.1641 | -54.4854 | 2024-11-08 02:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bf8f087b-07cf-3706-abc4-2045943033b1 | -3.967 | -48.15 | 2024-11-08 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bd052cf2-5f2a-3afb-ad44-8ad0b4f1e094 | -2.6948 | -51.8185 | 2024-11-08 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 79057716-b5ab-3f1c-a5cd-bbd5f57834d1 | -3.5631 | -47.3847 | 2024-11-08 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 84f4481b-8c64-31b3-b4f9-1edc32a588dc | -1.5165 | -52.0671 | 2024-11-08 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 40812732-a988-3520-88ae-ae454014bac5 | -1.1489 | -52.0099 | 2024-11-08 02:50:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 562a7149-5d3c-39c5-a151-33be68d4930b | -2.82 | -52.9613 | 2024-11-08 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e5a5214c-3dc6-3ffa-9bff-491732eb3198 | -3.9483 | -48.1724 | 2024-11-08 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 10f39efb-2d0a-3028-b0be-dec475ce65a1 | -3.5446 | -47.3855 | 2024-11-08 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 6a9e80d8-4a80-3fdc-be29-a34be55d6606 | -2.6764 | -51.8189 | 2024-11-08 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 892e39ba-f8b9-3d98-adb9-e2accdc01a21 | -3.9669 | -48.1716 | 2024-11-08 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| bf590f0d-36de-314e-8bda-785c5928a2d7 | -3.9485 | -48.1508 | 2024-11-08 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| c71a7b7c-075c-3f97-bc0f-30ebaeea90ea | -2.7832 | -52.9418 | 2024-11-08 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| fc7c68f5-dd80-3438-942b-0f07c46b6c69 | -4.5395 | -45.6794 | 2024-11-08 02:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 210f82ce-139a-3277-b5b6-379e1d4bc38f | -3.5632 | -47.3629 | 2024-11-08 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e518a266-128a-3555-bcf9-0f04906ef744 | -2.8016 | -52.9617 | 2024-11-08 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 16b0c82c-c3ef-3b62-bcc4-1307a5c54efd | -4.5207 | -45.7029 | 2024-11-08 02:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 139.3 |
| bd8f5f45-f284-3fe5-b189-9591b770841c | -2.82 | -52.9409 | 2024-11-08 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a4592358-179e-39bb-a560-8df4466af254 | -3.1641 | -54.4854 | 2024-11-08 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1cd1e449-670e-32ad-83e1-c9fdc194629a | -3.5447 | -47.3636 | 2024-11-08 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |


[Clique aqui para ver as próximas entradas](README12.md)
