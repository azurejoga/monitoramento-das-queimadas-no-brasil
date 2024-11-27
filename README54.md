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
| 52ce9535-f168-31c5-aa6e-269d05375836 | -3.23127 | -50.31725 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e10ecf7-313b-3d50-a9e2-cc6ce3801c02 | -1.75859 | -53.63243 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adfa779f-de94-3025-9b32-e6065b12e2da | -1.64454 | -52.1043 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e610838e-3fbd-3d0e-a315-af3e7c8b8b39 | -2.24066 | -53.63203 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7fa23fa2-dc49-359b-a77e-2f7a7002681b | -3.51873 | -50.21828 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a688cbb-9bec-3e35-9e50-bae1333aaf9d | -1.19756 | -51.76036 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ed2351b-89cc-30a9-aa38-c8401ffa22e2 | -2.60693 | -54.24661 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3660f3da-4cb4-305d-8695-aea01490512b | -4.22767 | -48.67441 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 546f66d5-0154-30e4-a1e6-7227711afa2e | -1.66429 | -52.71144 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19d0f165-b26d-3e27-85e8-c19be3720402 | -2.97208 | -51.57534 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5326e80f-038d-384a-839a-904b0d49e613 | -2.86371 | -46.81059 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebc7e26d-3b83-3b34-b89e-b476271668ee | -2.69407 | -51.87297 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dc95e1e-465f-3da4-9606-7fbf7e64bebf | -3.7162 | -51.80164 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4720a90b-2b8c-32fc-abc2-8887f509581e | -2.79164 | -51.68019 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ea9ac97-9796-3edc-b0dc-e0e93b64d578 | -1.26989 | -52.16382 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 987842ce-94c6-302f-9471-dc4945a943c2 | -3.49788 | -53.82482 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b09bb143-8092-38b1-ace5-f5f32a8389c2 | -3.71168 | -51.80829 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a311ec3f-d0fd-3ff5-b83d-8baf500099a7 | -5.49358 | -47.6582 | 2024-11-27 04:42:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2463c97-c3c1-37c9-a14f-42b37c25df7c | -1.78212 | -52.74572 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f066f6a-b1ee-3e75-918d-31098392e4ec | -1.77181 | -53.62101 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52b7781d-4d3d-3054-8eb9-948652e8343c | 0.16739 | -49.63364 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3130b6e8-63bb-3faf-a3a8-f9a5c4b2ab14 | -3.28538 | -51.1582 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5754200b-b82a-3594-a09a-0b5514d20857 | -1.42489 | -45.95913 | 2024-11-27 04:42:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd54ec26-0197-3718-96ae-6c3fe726cfa1 | -2.96922 | -48.00335 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20cfe2db-a584-3a36-96ca-bcdda4c22baf | -3.59018 | -50.60612 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dbd6f3a7-89a7-327c-80c0-d9287102ab2d | -1.54797 | -48.2877 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b51892c9-e2c0-3a44-8523-d1c1b589aedb | -2.33641 | -52.18159 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ce02bdd-8654-3f44-a5a2-d409804e7ef4 | -3.53743 | -50.40073 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 957937de-715e-34e8-bde1-4c9fa0bd53ed | -3.15773 | -49.2475 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcd41c0f-c08e-31f5-b3ff-ab49cea31708 | -3.23256 | -50.78315 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cda45ad1-3ad2-3f23-999e-164cbacd1bd5 | -4.23164 | -48.67128 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42a22792-85b0-3b9a-8a4d-01f12d6423a8 | -4.65735 | -46.8922 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8391bb8a-b8e9-37b9-9021-0b27c24d1368 | -3.25102 | -50.62345 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82b0c16e-f43f-3842-af73-d557b10a1320 | -3.03588 | -51.77336 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7acc024d-45a1-3b47-b390-0f9006a93ec5 | -2.89186 | -48.27407 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f83ad96-6fc0-31c4-8b71-a5291c0e2421 | -3.94669 | -46.9161 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60d4bf81-231b-335e-b3a2-c128daff13a5 | -1.06222 | -51.79684 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0170b8d-99bb-3fe5-b4de-821f761a3b26 | -0.94395 | -51.65675 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bba9b1f-c318-3077-90f5-0709ca17b5c7 | -3.99762 | -43.25529 | 2024-11-27 04:42:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39d6641b-6135-3f05-aca8-7035b997538b | -4.91697 | -47.85957 | 2024-11-27 04:42:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6bd20dd2-a908-3f85-80f1-6c8f32e91035 | -3.2474 | -53.29241 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf032337-d129-3ce4-b22b-b3903dc967a9 | -2.09359 | -46.32144 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4e6b818-b3a4-3d72-aea5-a69b0f626c3d | -1.30728 | -51.75401 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0cc9b66-bad3-32bf-9acf-1cb06ee60d86 | -4.72219 | -46.57032 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a5d31442-7731-396c-a6bb-9f8783d78f24 | -4.47574 | -46.66296 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e042bf74-9db1-343f-abab-fc96db0db738 | -1.95745 | -54.13902 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47e58161-d2c6-37e1-8666-a485361b963b | -2.4793 | -49.11346 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1f8dca3-8d24-304b-9fd0-0668c6524a6a | -1.66398 | -52.25179 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad1ebe44-dd37-3121-a428-54b753eec34c | -1.22978 | -51.95603 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8440480-1944-3df5-9831-993f47a2b426 | -2.99055 | -51.45779 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 295518fb-25d8-3898-8208-300656e51101 | -3.2343 | -51.60947 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c7ef2f2-1274-32c0-ab95-b17d3f1fdabe | -1.04641 | -51.741 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea55bf54-0eaf-3b0f-96a9-c990b2ae0166 | 0.95173 | -50.7568 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2e2e940-062e-3722-bbb5-9fe2854fe287 | -4.1571 | -53.47514 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be888af0-2cd3-348a-990f-660529624f9f | -1.61548 | -52.22056 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aa3cf76-8269-31e4-9bf8-192bba3065cb | -4.0002 | -47.9197 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4886ed7-1b49-39ab-8135-84492cdecd0c | -2.24785 | -53.61089 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72b87f4c-7116-39cc-bdde-01f17c4fc02f | -2.60459 | -53.97302 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74c952db-2484-3a48-b804-67faa7e40d67 | -3.26742 | -50.5625 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a73df81-8c96-389b-af05-48b8ff490f91 | -4.69588 | -44.96577 | 2024-11-27 04:42:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e1846c5-3442-3ab2-9c98-377a19912bd5 | -4.31462 | -47.51854 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2fca1d5e-494f-357f-84ad-7d1ed587030f | -4.22502 | -46.88322 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c376c1e9-ed97-3524-8d95-50cfc2890730 | -1.31243 | -51.74345 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eae82495-008d-3e30-8ba9-76660f8d645e | -3.24335 | -53.63861 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dbda4739-ebd0-35f8-9970-13dcc018c7a4 | -4.40383 | -48.30462 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 914d6ba4-8a16-3215-a69f-3445fbd95dc6 | -2.22359 | -53.62045 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78254b61-616b-3048-8001-f036d8f8c9bf | -3.54396 | -50.18699 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4d5402e-cbb4-3e46-9d95-c5ff3ee7b2dd | -2.68311 | -48.59714 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce351dd1-d79a-3277-b09f-c69ab6fe8865 | -3.57726 | -41.95614 | 2024-11-27 04:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| cbe3d526-0fc1-3e0f-91ae-ff432d71e90c | -3.3393 | -53.31569 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ef5b57-f97d-3324-84e8-0fbabcdd494c | -2.47652 | -49.10945 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8eb7c477-92bf-3ab7-95aa-50bbb3522a66 | -4.17408 | -48.45476 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b06ea8df-9b41-3e80-8294-99185b29942f | -3.75052 | -51.78131 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10eda3bc-8ce2-302c-9b1a-5732beafaa77 | -3.08724 | -53.25719 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8eb47e4a-0a81-383e-9822-2b6df0ffd0b6 | -3.44824 | -50.29875 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd5350f2-94ec-304d-93fb-45911fa55aaa | -3.22042 | -48.82233 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb525a86-08f0-3beb-8ea3-79b6cc01da51 | -1.2662 | -51.59301 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8a230cd-1769-3c94-bcf2-1985351127f0 | -2.60532 | -53.96852 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dce1bcd-9694-31c6-a110-cd07ba0f2eff | -3.98132 | -48.06676 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b171419-61c6-3e62-b70a-25d2f1f246f1 | -3.20598 | -51.33956 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8715084c-151d-324c-b849-91df2e5c1032 | -2.59047 | -54.05968 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c19e19ec-e3c5-3ce7-9f6b-2b59ff73fda0 | -2.81014 | -53.02074 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90e47df9-202e-3c8d-ab2c-314a4bef3f91 | -1.4607 | -52.69419 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3310f98f-76b4-38d3-853d-7cf78560ff0c | -2.82976 | -51.28833 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f28c67d-2fcb-3a8a-a0f8-1fc4a0ed9735 | -1.94411 | -45.72924 | 2024-11-27 04:42:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 2d3a982f-ec44-363d-8ceb-9af4ef81465a | -2.22848 | -53.68401 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d071596b-9739-3e69-9cb8-177ddbbf9a2e | -2.89378 | -54.17418 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7724c98-d26c-321f-9b01-1e9c4c1dac88 | -2.68479 | -45.65376 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e14eb688-0f9f-39d7-bf17-9eb531fb5c72 | -3.87306 | -50.14687 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5020d64d-205d-3e95-bcc7-97919f950d18 | -2.25943 | -53.7523 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 00e7f7c8-3254-372f-811d-744b428347eb | -3.09865 | -53.25481 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fb6689ff-b3a7-381d-bc52-68e779feec26 | -3.3466 | -50.51139 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d6199a3-4f15-39ac-937c-9d2894875028 | -1.7175 | -53.60318 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 83bc6f2f-a8e7-39ec-bc72-bf2007f5f7c6 | -3.2065 | -53.37601 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0057d57b-7b3a-3d47-80a6-3fa824729475 | -4.11491 | -47.9721 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51246084-9638-351c-9e0e-ae1991e416eb | -4.29826 | -48.23861 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04d450af-6e8f-3b52-893d-2b6f08ac939b | -3.09732 | -53.73145 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c470f8f2-a6c5-3502-bfb0-97499b3f3181 | -3.18221 | -48.4346 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1287c27d-81ba-3cf9-a164-76abbb1bbd48 | -1.20272 | -51.74977 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a6bbabd-54b9-3778-9d11-bde3ba7ce6ab | -2.55211 | -46.4072 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README55.md)
