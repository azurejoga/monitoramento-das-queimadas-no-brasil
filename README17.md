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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2736ec58-9eb5-375a-9f97-11d91559dafe | -6.1229 | -43.9578 | 2024-12-03 02:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 693276b1-42e8-3a61-bf2f-4e1621b05683 | -2.8013 | -53.043 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 66bb6d5f-0b36-3448-9182-fd9e670c8cda | -2.8485 | -45.3963 | 2024-12-03 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| c7b5082d-25a7-3285-8faa-6c3f7a5eea0f | -3.076 | -53.4011 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1b1ef3ee-ffc5-3ec6-8b91-8167db26ce37 | -3.5682 | -50.1693 | 2024-12-03 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f6c2aa8a-550d-3d7b-a7b1-c077eb45c8b0 | -2.8012 | -53.0633 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c12308b7-8b57-3593-9d14-7920a93a2663 | -1.8052 | -46.671 | 2024-12-03 02:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 32f2023b-49a4-31c0-9079-16e964e10e6f | -1.7867 | -46.6714 | 2024-12-03 02:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| d8b62770-abe7-3675-89aa-92391f915d21 | -2.7377 | -45.2201 | 2024-12-03 02:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a8891d50-7927-30c4-91b8-f2839ab0c5f6 | -9.374 | -57.5553 | 2024-12-03 02:00:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c43f4872-7396-3940-bfb8-0ad2d0d5f55c | -1.7868 | -46.6494 | 2024-12-03 02:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fdb017ef-f39f-316c-aa69-3b21af31a6e8 | -5.801 | -46.4719 | 2024-12-03 02:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a11b104f-399c-3636-9dd3-144986fcd266 | -6.1229 | -43.9578 | 2024-12-03 02:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f22443b4-4c16-3823-97c4-afca10c173ab | -3.5496 | -50.191 | 2024-12-03 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 39a8b3d6-4c98-339c-aefd-7c428dbdffe0 | -3.1948 | -51.1637 | 2024-12-03 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| f7d0a37c-39c5-3013-b6f0-4905b3123109 | -2.8854 | -45.44 | 2024-12-03 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 59019fea-331c-3c9f-a1eb-fdc62f81947e | -3.347 | -46.0486 | 2024-12-03 02:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 730ff176-037e-30a2-955a-001a5e3377e0 | -3.0949 | -53.2385 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 86226510-7cb5-34bd-b210-a9a71995e11b | -5.8009 | -46.4941 | 2024-12-03 02:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| bdcb6a93-a7ab-3221-a105-bbc69442f271 | -1.8053 | -46.649 | 2024-12-03 02:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| ea388dfa-ad9b-34fe-8683-0b839d4cc267 | -2.8212 | -52.5741 | 2024-12-03 02:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| af4b6531-fbe2-35d9-8f91-33cf54e0070c | -4.1914 | -51.1914 | 2024-12-03 02:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4a05a813-9f13-33fd-bcfc-4ad230354138 | -4.1684 | -48.5937 | 2024-12-03 02:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 800e85a0-aafd-38e9-b300-61ddf8d55db8 | -3.076 | -53.3808 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| e03e80bf-4d01-3d3b-a282-df54ab0590c6 | -3.259 | -53.6388 | 2024-12-03 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 3809557f-6786-3b57-b107-45fb7224c6e8 | -5.8195 | -46.4929 | 2024-12-03 02:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a8a1db72-ad7d-3f7a-9567-cf3f681f5c68 | -2.8013 | -53.043 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9865251b-7b77-338c-8e25-6ba654bf77d9 | -1.7867 | -46.6714 | 2024-12-03 02:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c5178016-7763-35c7-87ad-279ad44c50ec | -5.8197 | -46.4706 | 2024-12-03 02:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f252fc88-227a-3154-917e-5001fad4ace0 | -2.8212 | -52.5945 | 2024-12-03 02:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| e7ce3d3a-c5e2-3b5a-b0ce-61f3feda1494 | -1.7541 | -52.7993 | 2024-12-03 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ee3eda59-a6bc-3588-8c78-1b7666ee313c | -12.7147 | -58.2231 | 2024-12-03 02:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 964d0df7-a226-341e-a528-f795c18eeeaa | -3.2591 | -53.6186 | 2024-12-03 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c1234204-bd06-385a-bfa6-3adc5a9f42d2 | -3.5497 | -50.1699 | 2024-12-03 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| ea50341e-367c-324e-9d8d-28b39d84233b | -2.8196 | -53.0629 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a94b95d9-9a6c-3507-b774-d6f1bfcb019b | -3.259 | -53.659 | 2024-12-03 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 50f3b419-ccef-3795-8c40-f28a6b32244b | -3.2775 | -53.6181 | 2024-12-03 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6daccab0-fc52-3d4f-b850-4b242c0344d5 | -6.9908 | -43.5349 | 2024-12-03 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a9d6b53f-9b84-3658-8b8c-789f577dfd91 | -11.4355 | -55.9098 | 2024-12-03 02:10:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ba937627-fc4c-3c4e-bed0-fd78579f8d06 | -2.7192 | -45.1982 | 2024-12-03 02:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 111.6 |
| d8cb997f-d734-371b-ac02-ba894e9ce225 | -2.7191 | -45.2208 | 2024-12-03 02:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| bf9c81d7-a054-3ab6-b7a1-a9fee886a4c4 | -12.7149 | -58.2032 | 2024-12-03 02:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cfdec893-e83c-3341-b3ff-71147b597ca7 | -2.7377 | -45.2201 | 2024-12-03 02:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 7561e611-9922-31be-a833-3f85f25e0260 | -3.0944 | -53.3804 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| ac48d94e-501d-37f2-8bf3-3665a4233e95 | -1.8052 | -46.671 | 2024-12-03 02:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e14bb67f-a4dc-3449-93f3-19052b808fd5 | -2.8197 | -53.0425 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c2b2af25-4040-31f8-ad92-345607703c9b | -5.801 | -46.4719 | 2024-12-03 02:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1f51d5d1-6bb0-3e5a-8b56-a7163445059f | -3.0761 | -53.3606 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 19cf3195-1b91-3c49-b508-b3ac4c177c01 | -6.9911 | -43.5116 | 2024-12-03 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 0dc20e04-8c88-3860-a826-7eb31c79cde5 | -1.7868 | -46.6494 | 2024-12-03 02:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| b556edd0-92dc-371c-9cd1-e69b56ba80d5 | -2.8853 | -45.4624 | 2024-12-03 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 08d828fa-1ea9-3c6d-ba94-9ef1fe5020fb | -2.8012 | -53.0633 | 2024-12-03 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 140c1720-e76e-3316-96ff-409192c67d96 | -3.0376 | -53.8664 | 2024-12-03 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| cde8f8fe-fcc6-38a1-9b1a-e46c83f3f26e | -4.5402 | -42.93 | 2024-12-03 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e84d55e7-c175-3701-b511-47418af89ef8 | -2.8485 | -45.3963 | 2024-12-03 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 108.0 |
| df969df8-7942-3b40-a879-0c8a158ac044 | -2.7378 | -45.1976 | 2024-12-03 02:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 127.1 |
| f67ccfa4-9d9b-32bd-9d67-7995b99b67e4 | -9.374 | -57.5553 | 2024-12-03 02:10:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c8dfe4b3-856d-394f-96d0-828ad37e6225 | -3.2774 | -53.6383 | 2024-12-03 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e65b2318-528c-3396-bdb3-168b8395580c | -3.5682 | -50.1693 | 2024-12-03 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 34533a38-cb12-3175-810b-76a8715acbd4 | -5.8197 | -46.4706 | 2024-12-03 02:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3f411f5c-4f25-322d-8ddb-0709c1456550 | -2.7192 | -45.1982 | 2024-12-03 02:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 411.2 |
| 23a56775-934c-3ed2-8f1c-7832218ba9c0 | -2.8853 | -45.4624 | 2024-12-03 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2319327b-3d25-336a-9912-815a598c6837 | -3.347 | -46.0486 | 2024-12-03 02:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 86.3 |
| b7861884-0489-3960-8c63-dbb00d0322b0 | -2.8212 | -52.5945 | 2024-12-03 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 36f8c210-c2a6-37dd-aeda-c4e01b593db4 | -2.8012 | -53.0633 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 19beaf5e-513c-3625-bb63-9aa157891ddd | -2.8013 | -53.043 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8286d884-df31-3cf7-9528-570ba3b3ffdd | -11.4355 | -55.9098 | 2024-12-03 02:20:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 944d3e68-86d5-375c-bc3d-8a7ae0598cee | -5.8009 | -46.4941 | 2024-12-03 02:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 01561246-9492-33fe-b233-a60d66902483 | -6.1229 | -43.9578 | 2024-12-03 02:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8a223dec-bd1b-3942-a32b-7efc55fd461b | -2.8212 | -52.5741 | 2024-12-03 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| fca48c39-535b-3e23-92c3-b12ebf3eae97 | -1.7541 | -52.7993 | 2024-12-03 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| de632ce5-e316-3a12-aa85-975127284545 | -3.259 | -53.659 | 2024-12-03 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 63a1c312-d44d-3e7e-8de2-255fd06bbce2 | -2.7191 | -45.2208 | 2024-12-03 02:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 295.2 |
| edc9c07e-cee6-3d1f-aa43-12cc451d78fe | -1.7867 | -46.6714 | 2024-12-03 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a6e02eae-dd95-3301-80d2-64ddeb3fcd9a | -2.8196 | -53.0629 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| ab573ec3-9a50-368b-96ae-30f31f8cea06 | -2.7378 | -45.1976 | 2024-12-03 02:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 345.1 |
| bbb3f2a6-e0cd-3209-9e20-a48f2e3f83e3 | -2.8485 | -45.3963 | 2024-12-03 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 6936914b-63b6-3a58-b336-50519ff85058 | -2.7377 | -45.2201 | 2024-12-03 02:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 255.6 |
| 69d61c04-db7f-338a-964f-9e0b20072470 | -4.1914 | -51.1914 | 2024-12-03 02:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| bd423921-abd1-3e82-a000-fd69736a266f | -2.8197 | -53.0425 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ab0e876d-80f2-31e5-8744-877c020174b4 | -3.2591 | -53.6186 | 2024-12-03 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f4b68ecf-a18c-3848-9de4-d6d3d0f6444d | -3.5496 | -50.191 | 2024-12-03 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 25f89514-55d4-3652-9e8e-8413d1911c02 | -2.8854 | -45.44 | 2024-12-03 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 1e1aaa13-f4b4-3363-b218-68c484b89d91 | -3.5682 | -50.1693 | 2024-12-03 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| fcc32efe-b8f1-30b1-830e-9874f0bb4c6b | -1.7361 | -52.6366 | 2024-12-03 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fd42ebc9-fa0e-3922-8347-d1bdc15c97e4 | -3.0944 | -53.3804 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 8f3dccec-a7b7-3beb-ad8c-27cfcb88dac1 | -3.076 | -53.3808 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| f18ec5e9-adeb-3d14-b1f5-6c7f62f4e3bc | -3.259 | -53.6388 | 2024-12-03 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 3f774a5a-1b6d-37bb-8745-a1ba4d8d0d36 | -3.0945 | -53.3601 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fb5e5fe9-d5bb-3cf7-976d-23ae3f553cd0 | -2.8486 | -45.3739 | 2024-12-03 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 186c642b-2b86-3298-ae66-8db1321cece8 | -1.8053 | -46.649 | 2024-12-03 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 280.6 |
| 60d88a50-c45a-3796-b595-8078bca93aa3 | -5.801 | -46.4719 | 2024-12-03 02:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 01c1ae76-4e7c-35f9-b7f9-9098db5aa5f4 | -4.1915 | -51.1706 | 2024-12-03 02:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 647ab905-8e96-3046-9b5b-980841bbebda | -3.0761 | -53.3606 | 2024-12-03 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 6fd3d402-dcbe-3981-8fb7-115aee3e9a0b | -1.7868 | -46.6494 | 2024-12-03 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 4f84647d-04aa-3689-9790-18352b3e084f | -3.5681 | -50.1903 | 2024-12-03 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5f619a0b-ebc6-374e-a260-a4ab63bce260 | -3.5497 | -50.1699 | 2024-12-03 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| dec1795e-9b86-391d-9ee8-fd02b91edbff | -1.8052 | -46.671 | 2024-12-03 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| a285cb65-71e2-3e14-aa9e-0632e1c6c26f | -9.374 | -57.5553 | 2024-12-03 02:20:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 61afcad4-29c9-3e77-a7db-c8787456b849 | -2.7377 | -45.2201 | 2024-12-03 02:30:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 259.6 |


[Clique aqui para ver as próximas entradas](README18.md)
