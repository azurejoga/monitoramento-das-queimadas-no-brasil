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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9f63f33-2db2-3eb3-9ef5-270ff99c4696 | -3.0947 | -53.3196 | 2024-11-08 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 46f1f7b4-04e0-37ab-8705-f485074a2b01 | -4.6832 | -46.4518 | 2024-11-08 01:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 300.3 |
| 18e86dfa-e055-315e-9b51-12334b3333a9 | -4.5209 | -45.6804 | 2024-11-08 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 535.8 |
| b8914a64-cfaf-3f04-af2b-922910b4c8bd | -2.82 | -52.9409 | 2024-11-08 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| e57511f4-c567-3a86-91c4-3f57a48d98af | -4.7018 | -46.4508 | 2024-11-08 01:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| b11bdd6f-5b93-37ce-a784-9c4743926f7b | -3.1458 | -54.4859 | 2024-11-08 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f858e3af-20a4-3854-a29d-a5c27dab5bdc | -4.5021 | -45.7039 | 2024-11-08 01:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b7a70652-b578-345d-ba73-dd427f111400 | -3.1641 | -54.4854 | 2024-11-08 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e19cbc59-cd40-352e-8164-adad8df6e898 | -2.7832 | -52.9418 | 2024-11-08 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 617a11da-267c-3718-a5a4-0866682487ab | -3.0698 | -45.747 | 2024-11-08 01:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c4d864a9-bdec-3890-87b6-183cdec25f1c | -4.6269 | -46.5213 | 2024-11-08 01:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 29bce2c1-b142-3e39-adab-2dfa3ca4b34b | -4.6832 | -46.4518 | 2024-11-08 01:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 233.5 |
| 83d53edc-d1c2-3531-863f-86d88fac7e00 | -2.82 | -52.9409 | 2024-11-08 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 7f884fe0-fcac-36d0-8872-406cf270a235 | -1.1489 | -51.9894 | 2024-11-08 01:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3ae18fb3-7281-356c-a6d2-0dfff6af21f9 | -3.5446 | -47.3855 | 2024-11-08 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| c57df57e-ba6d-3327-a930-c4cc0bfd6d40 | -2.8016 | -52.9414 | 2024-11-08 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 232.8 |
| d4957487-7437-3f60-8058-74c0b38a7a86 | -2.8016 | -52.9617 | 2024-11-08 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 5784b135-78c0-3074-a27c-c16455fab9fd | -2.7832 | -52.9418 | 2024-11-08 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 683b04e0-5d4e-3ae1-9ea8-6b575c8bacbf | -3.7254 | -41.6987 | 2024-11-08 01:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 00def9d3-b76e-3530-a0a3-7ff18a655a70 | -3.5631 | -47.3847 | 2024-11-08 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 8436f04a-7129-3645-881f-75a57d73c66f | -3.9485 | -48.1508 | 2024-11-08 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4c466396-c03d-3965-9e5b-f690af48627f | -3.9669 | -48.1716 | 2024-11-08 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| a50c4de4-04b4-3671-b27f-f96568bb7b71 | -6.264 | -39.3797 | 2024-11-08 01:20:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 22af50f8-c2fe-3b7a-b898-fedaf28f2ce3 | -3.7255 | -41.6748 | 2024-11-08 01:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 177f6e65-1d92-3ff3-99f1-8c88e25a7292 | -3.1458 | -54.4859 | 2024-11-08 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d177872b-8b6e-3216-a0d5-56a639ff8152 | -3.967 | -48.15 | 2024-11-08 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9885dcb4-cb67-33b2-8874-077246f77f8b | -3.1642 | -54.4654 | 2024-11-08 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 6a15d320-afb4-38fb-9861-75e725252334 | -3.9854 | -48.1708 | 2024-11-08 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a4cb2602-70e1-378e-9615-12ccea321279 | -1.1489 | -52.0099 | 2024-11-08 01:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 67990332-56fa-3e67-b434-55084dd9c4fb | -2.82 | -52.9613 | 2024-11-08 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 19b1578a-1960-3483-9798-dccb677ab216 | -3.1641 | -54.4854 | 2024-11-08 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 49bde0f6-1b90-318e-9f99-b85698959b38 | -4.6834 | -46.4296 | 2024-11-08 01:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 6964c3e6-87af-3165-a7d6-eae13a892a20 | -3.5632 | -47.3629 | 2024-11-08 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3253d241-2779-3889-8077-fb4bb827820d | -3.9483 | -48.1724 | 2024-11-08 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 90085ab7-3313-3176-9b5d-9c3fcbb282ad | -3.5447 | -47.3636 | 2024-11-08 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5a0d80dc-d82a-3bdd-8f29-2978cc73288b | -4.5022 | -45.6815 | 2024-11-08 01:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 182.0 |
| ac9604cf-ea9e-387d-92ed-c557c574781b | -2.8016 | -52.9617 | 2024-11-08 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 53dff1e9-7776-3b67-9d96-20f08e68319f | -3.9854 | -48.1708 | 2024-11-08 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e65f7793-0c7c-3624-b301-c98bc7e46829 | -2.6228 | -51.3038 | 2024-11-08 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 995bb7b8-ddd0-3da8-ab43-9cbe5aacf223 | -5.9909 | -46.1024 | 2024-11-08 01:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| bf548ac0-48f4-33a5-b22c-f137b6048102 | -1.1489 | -52.0099 | 2024-11-08 01:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fca94bdd-bf16-3171-82d8-f1e1a1032271 | -3.9669 | -48.1716 | 2024-11-08 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 3940d207-51c2-3490-b6ac-a29dbc442358 | -1.1489 | -51.9894 | 2024-11-08 01:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 65de55d3-dd56-351c-9a91-0699dcf77022 | -6.264 | -39.3797 | 2024-11-08 01:30:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 36.6 |
| d7dc7560-3c9c-3039-ac18-f8469605b5fa | -2.9425 | -45.1453 | 2024-11-08 01:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 08963403-5c40-300a-846b-06c084027702 | -3.0698 | -45.747 | 2024-11-08 01:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 6f80354b-20ad-3cfa-803f-8791873e352f | -3.5447 | -47.3636 | 2024-11-08 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 239e9b06-87e4-3cf4-800d-7261ff1c6242 | -3.9483 | -48.1724 | 2024-11-08 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 35d95ac1-6e86-3b86-ba2b-a1dd5d55d826 | -3.967 | -48.15 | 2024-11-08 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8a7f8a2a-47b6-389b-808b-003d75b6e91f | -4.5207 | -45.7029 | 2024-11-08 01:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 54b1ca3d-f4a6-3b4f-9e30-27a9cb5238e4 | -5.9911 | -46.08 | 2024-11-08 01:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4d443c41-a64d-388a-9501-c4e17f56af08 | -3.0274 | -51.5415 | 2024-11-08 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3f37e499-b970-31de-b3ff-dfc266dc658f | -3.5632 | -47.3629 | 2024-11-08 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 5b41deb1-479a-3ac3-a336-a3ccf43c1b85 | -2.82 | -52.9409 | 2024-11-08 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 2ec193c3-22c4-3554-adfb-f3639e3f0435 | -2.8016 | -52.9414 | 2024-11-08 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 219.4 |
| 50f80e97-3f2a-3bcb-8abc-52b7a42e1bec | -4.6834 | -46.4296 | 2024-11-08 01:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 3d0f398e-efae-3098-9472-b200922a7f84 | -3.9485 | -48.1508 | 2024-11-08 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 09fb1fcd-bf3f-3ed3-8b9d-b94bf3dc82fe | -4.5395 | -45.6794 | 2024-11-08 01:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 7f211d66-8061-315d-9e63-2ca297402926 | -3.1641 | -54.4854 | 2024-11-08 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 55ac8817-b2d8-33c9-8f32-f25ce1ef7489 | -4.6832 | -46.4518 | 2024-11-08 01:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 8e55c6ff-0e2f-3f62-a8b6-f9484c9bde46 | -3.7254 | -41.6987 | 2024-11-08 01:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| a1d7816f-cafa-3d4c-a6ed-b7a8afc38ca1 | -3.5446 | -47.3855 | 2024-11-08 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 537c89a1-073c-3e39-8d15-b7545bed5632 | -4.5021 | -45.7039 | 2024-11-08 01:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 401b7a84-b161-3298-afa1-48c5bbf83b9a | -4.521 | -45.658 | 2024-11-08 01:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 647ab969-8842-3328-a72f-a87b3bdeb749 | -1.1673 | -52.0098 | 2024-11-08 01:30:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1e923d44-5a7f-3251-9fd8-a3a4182d2e61 | -2.82 | -52.9613 | 2024-11-08 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| d4d40e27-2883-3165-917e-060b0731305b | -3.5631 | -47.3847 | 2024-11-08 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 17ce0041-16e0-35df-9d6d-fc3dfb320bcd | -3.1642 | -54.4654 | 2024-11-08 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| cf07234b-7ac5-3fdb-adb5-948b2ddb031b | -4.5209 | -45.6804 | 2024-11-08 01:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 352.6 |
| 6870b993-a265-361e-b434-24c8c0e65d61 | -1.72876 | -54.15166 | 2024-11-08 01:36:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b3683b7a-5d0d-3754-82cf-39cf98a81774 | -3.01651 | -53.44571 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 21639d83-3873-3564-b218-cacb38e79e3b | -7.87615 | -61.68202 | 2024-11-08 01:36:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 714a1173-5edd-39ed-a453-dee3497e4594 | -1.39147 | -52.20062 | 2024-11-08 01:36:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| f182eb55-a280-3144-b933-41b9abd8c43f | -2.2193 | -53.732 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d029162e-db50-3137-b889-8103603d8973 | -2.81411 | -52.95654 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 11623502-ee3e-309c-9c09-36ee65dab23b | -3.15218 | -54.47228 | 2024-11-08 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 803464af-a7ff-378f-8bfc-6abe6cc04bfc | -2.25855 | -53.72059 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 89aa3f9a-a4e0-3deb-8b5b-8da1a0b0aa0f | -1.59411 | -53.74656 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f6e004f4-dc37-3695-8af9-d28064ab3757 | -1.45451 | -53.42115 | 2024-11-08 01:36:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 43f792b7-679b-35d3-abae-0c65ad4f5c82 | -3.09183 | -53.33167 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b5e65042-8528-30b1-a54a-38b984a2a4b6 | -2.25662 | -53.72651 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 07758981-e9c1-36ac-9f24-adcdb5d75bed | -7.87454 | -61.67694 | 2024-11-08 01:36:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f24083bd-9c7c-3647-a004-e4aced354966 | -7.92841 | -61.46959 | 2024-11-08 01:36:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| df573448-fd1d-3145-be77-f19e28f7c3ed | -2.76682 | -54.04951 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c507d09c-2781-36af-9988-6f878e5f6e17 | -1.59125 | -53.72739 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b5d8a0ff-aec6-3cf0-96db-9885435e9771 | -2.94703 | -52.70774 | 2024-11-08 01:36:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| cfa88d57-b4bb-33c5-920b-191642247d4b | -1.59031 | -53.73418 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| d609475d-f38f-3825-8a36-dbebbe249295 | -7.92692 | -61.45857 | 2024-11-08 01:36:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d9e69137-c2dc-3fab-bbdb-a318c0c45fe1 | -2.77631 | -54.03067 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e759ebe8-b87a-3bac-8941-56599d7c9fbe | -2.15576 | -53.64614 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 1755d046-49b2-3a6c-8303-c93c14b186b0 | -3.16368 | -54.47044 | 2024-11-08 01:36:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 85e21720-d3d8-3bce-a680-33a35bf66b6e | -2.64585 | -54.78624 | 2024-11-08 01:36:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c76e4127-d7e3-3179-860d-37fef4306709 | -2.05093 | -53.29078 | 2024-11-08 01:36:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 08a2101e-8e0f-3bcd-9b71-11661c88e170 | -1.45282 | -53.41573 | 2024-11-08 01:36:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1d608e69-379e-3dcb-b4c1-9986a1b5c085 | -2.05384 | -53.31084 | 2024-11-08 01:36:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 00aebb2b-2006-3ccc-a2a0-a1aa962d84a2 | -1.14665 | -51.98439 | 2024-11-08 01:36:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| b1ebc78d-f5df-3bbb-a75c-b2fe491d9dbd | -2.81709 | -52.9767 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| e7487730-9ecd-34e5-bc0d-151aab9f60b7 | -2.15455 | -53.65282 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 05684063-05c3-3593-8f80-42fb6c071012 | -3.09217 | -53.32605 | 2024-11-08 01:36:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 5308d50d-e25b-30df-ae7f-5d15ad619012 | -2.76428 | -54.03237 | 2024-11-08 01:36:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README10.md)
